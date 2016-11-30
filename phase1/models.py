from colorfield.fields import ColorField
from django.db import models
from solo.models import SingletonModel


class Category(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class News(models.Model):
    title = models.CharField(max_length=300)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)
    categorized = models.BooleanField()
    categories = models.ManyToManyField(to='Category', related_name='news', blank=True)
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


class Config(SingletonModel):
    categorized_urls_num = models.IntegerField(default=10,
                                               verbose_name='Number of categorized '
                                                            '(phase 1) urls for each team')
    uncategorized_urls_num = models.IntegerField(default=10,
                                                 verbose_name='Number of uncategorized '
                                                              '(phase 3) urls for each team')
    max_news_count_per_team = models.IntegerField(default=500,
                                                  verbose_name='Maximum number of news for each '
                                                               'team')

    background_color = ColorField(default='#3d5050', verbose_name='Background color')
