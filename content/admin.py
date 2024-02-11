from django.contrib import admin

from content.models import Txt, Titles


@admin.register(Txt)
class TxtAdmin(admin.ModelAdmin):
    list_display = 'title', 'tag', 'active'
    list_display_links = 'title', 'tag'


@admin.register(Titles)
class TitleAdmin(admin.ModelAdmin):
    list_display = 'title', 'tag'
    list_display_links = 'title', 'tag'
