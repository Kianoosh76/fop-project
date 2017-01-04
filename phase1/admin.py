from django.contrib import admin
from solo.admin import SingletonModelAdmin

from phase1.models import CategorizedURL, UncategorizedURL, News, Category, Config, LearningURL

admin.site.register(Category)
admin.site.register(News)
admin.site.register(CategorizedURL)
admin.site.register(UncategorizedURL)
admin.site.register(LearningURL)
admin.site.register(Config, SingletonModelAdmin)
