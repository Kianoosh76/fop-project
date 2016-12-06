from django.contrib import admin

from phase0.models import Text
from teams.models import Team


class TeamsInline(admin.StackedInline):
    model = Team
    fields = ['id']
    extra = 0


class TextAdmin(admin.ModelAdmin):
    readonly_fields = ['smallest_repeated_word', 'distinct_longest_words']
    list_display = ['__str__', 'smallest_repeated_word', 'distinct_longest_words']
    inlines = [TeamsInline]

admin.site.register(Text, TextAdmin)
