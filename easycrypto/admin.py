from django.contrib import admin

from easycrypto.models import Expertise


@admin.register(Expertise)
class QuesAdmin(admin.ModelAdmin):
    list_display = 'order', 'image', 'title', 'text', 'published', 'updated'
    list_display_links = 'image', 'title', 'text'

