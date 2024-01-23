from django.contrib import admin
from contacts.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = 'theme', 'active'
    list_display_links = 'theme',
