from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

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
    actions = ['generate_password', 'add_text', 'assign_categorized_urls',
               'assign_uncategorized_urls']
    readonly_fields = ['answer1', 'answer2', 'categorized_urls', 'uncategorized_urls']

    def generate_password(self, request, queryset):
        for team in queryset:
            team.user.set_password(team.generate_password())
            team.user.save()
    generate_password.short_description = 'Generate password for selected teams'

    def answer1(self, obj):
        return obj.text.smallest_repeated_word

    def answer2(self, obj):
        return obj.text.distinct_longest_words

    def add_text(self, request, queryset):
        for team in queryset:
            team.add_text()
            team.save()
    add_text.short_description = 'Add/change phase 0 text for selected teams'

    def assign_categorized_urls(self, request, queryset):
        for team in queryset:
            team.assign_categorized_urls()
            team.save()
    assign_categorized_urls.short_description = 'Assign categorized (phase 1) urls to' \
                                                ' selected teams'

    def assign_uncategorized_urls(self, request, queryset):
        for team in queryset:
            team.assign_uncategorized_urls()
            team.save()
    assign_uncategorized_urls.short_description = 'Assign uncategorized (phase 3) urls to ' \
                                                  'selected teams'


class NewUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('last_login',)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Member)
admin.site.register(Vote)
