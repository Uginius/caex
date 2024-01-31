from django.contrib import admin
from contacts.models import Subject, Smm, Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = 'created', 'name', 'account', 'subject', 'message'
    list_display_links = 'created', 'name', 'account', 'subject', 'message'


@admin.register(Smm)
class SmmAdmin(admin.ModelAdmin):
    list_display = 'order', 'name', 'account', 'style'
    list_display_links = 'name', 'account', 'style'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = 'theme', 'active'
    list_display_links = 'theme',
