from django.contrib import admin

from phase1.models import News
from teams.models import Team, Member, Vote


class MemberInline(admin.TabularInline):
    model = Member
    extra = 2


class NewsInline(admin.TabularInline):
    model = News
    extra = 0
    exclude = ['categories']
    readonly_fields = ['all_categories']


class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [MemberInline, NewsInline]
    list_display = ['__str__', 'votes']
    actions = ['generate_password']

    def generate_password(self, request, queryset):
        for team in queryset:
            team.user.set_password(team.generate_password())
            team.user.save()
    generate_password.short_description = 'Generate password for selected teams'

admin.site.register(Team, TeamAdmin)
admin.site.register(Vote)