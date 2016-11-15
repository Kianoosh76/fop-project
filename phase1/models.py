from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class News(models.Model):
    title = models.CharField(max_length=300)
    date = models.CharField(max_length=40)
    description = models.TextField(max_length=2000)
    categorized = models.BooleanField()
    categories = models.ManyToManyField(to='Category', related_name='news', null=True, blank=True)
    team = models.ForeignKey(to='teams.Team', related_name='news')

    class Meta:
        verbose_name_plural = 'News'

    @property
    def all_categories(self):
        return " ".join([str(category) for category in self.categories.all()])

    def __str__(self):
        return self.title


class URL(models.Model):
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.url


class CategorizedURL(URL):
    pass


class UncategorizedURL(URL):
    pass