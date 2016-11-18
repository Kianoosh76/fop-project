from Crypto.Random.random import randint
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL

from phase0.models import Text


class Team(models.Model):
    user = models.OneToOneField(to=User, blank=True, related_name='team')
    name = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    text = models.ForeignKey(to='phase0.Text', null=True, blank=True, related_name='teams',
                             on_delete=SET_NULL)

    def generate_password(self):
        return "_".join([str(member.student_id) for member in self.members.all()])

    def add_text(self):
        texts = Text.objects.count()
        if texts > 0:
            self.text = Text.objects.all()[randint(0, texts-1)]

    def save(self, *args, **kwargs):
        if self.id is None:
            count = 0
            last_team = Team.objects.last()
            if last_team:
                count = last_team.pk
            self.user = User.objects.create_user(username='team' + str(count+1),
                                                 password='')

        if not self.text:
            self.add_text()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}: {}".format(self.user.username, self.name)


class Member(models.Model):
    name = models.CharField(max_length=40)
    student_id = models.IntegerField(unique=True)
    team = models.ForeignKey(to='Team', null=False, related_name='members')

    def __str__(self):
        return "{}: {}".format(self.student_id, self.name)


class Vote(models.Model):
    member = models.ForeignKey(to='Member', null=False, related_name='votes')
    team = models.ForeignKey(to='Team', null=False, related_name='votes_list')
    valid = models.BooleanField(default=True)

    class Meta:
        unique_together = ['member', 'team']

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.team.votes += 1
            self.team.save()
        else:
            old_object = Vote.objects.get(pk=self.pk)
            if old_object.valid and not self.valid:
                self.team.votes -= 1
            elif not old_object.valid and self.valid:
                self.team.votes += 1
            self.team.save()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.valid:
            return '{} VOTED TO {}'.format(str(self.member), str(self.team))
        else:
            return 'Invalid vote'
