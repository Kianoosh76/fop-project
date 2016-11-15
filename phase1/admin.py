from django.contrib import admin

from phase1.models import CategorizedURL, UncategorizedURL, News, Category

admin.site.register(Category)
admin.site.register(News)
admin.site.register(CategorizedURL)
admin.site.register(UncategorizedURL)