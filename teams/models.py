from Crypto.Random.random import randint, shuffle
from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models.deletion import SET_NULL

from phase0.models import Text
from phase1.models import CategorizedURL, Config, UncategorizedURL


class Team(models.Model):
    user = models.OneToOneField(to=User, blank=True, related_name='team')
    name = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    text = models.ForeignKey(to='phase0.Text', null=True, blank=True, related_name='teams',
                             on_delete=SET_NULL)
    categorized_urls = models.ManyToManyField(to='phase1.CategorizedURL', related_name='teams')
    uncategorized_urls = models.ManyToManyField(to='phase1.UnCategorizedURL', related_name='teams')

    def generate_password(self):
        return "_".join([str(member.student_id) for member in self.members.all()])

    def assign_categorized_urls(self):
        urls = CategorizedURL.objects.order_by('?')
        self.categorized_urls.clear()
        for i in range(min(len(urls), Config.get_solo().categorized_urls_num)):
            self.categorized_urls.add(urls[i])

    def assign_uncategorized_urls(self):
        urls = UncategorizedURL.objects.order_by('?')
        self.uncategorized_urls.clear()
        for i in range(min(len(urls), Config.get_solo().uncategorized_urls_num)):
            self.uncategorized_urls.add(urls[i])

    def add_text(self):
        texts = Text.objects.count()
        if texts > 0:
            self.text = Text.objects.all()[randint(0, texts - 1)]

    def save(self, *args, **kwargs):
        if self.id is None:
            count = 0
            last_team = Team.objects.last()
            if last_team:
                count = last_team.pk
            self.user = User.objects.create_user(username='team' + str(count + 1),
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

    def votes_list(self):
        return [(vote.team.id, vote.valid) for vote in self.votes.all()]


class Vote(models.Model):
    member = models.ForeignKey(to='Member', null=False, related_name='votes')
    team = models.ForeignKey(to='Team', null=False, related_name='votes_list')
    valid = models.BooleanField(default=True)

    class Meta:
        unique_together = ['member', 'team']

    def save(self, *args, **kwargs):
        with transaction.atomic():
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
