from django.contrib import admin

from main.models import CoinService, Step


@admin.register(CoinService)
class CoinAdmin(admin.ModelAdmin):
    list_display = 'title', 'caption', 'icon', 'is_banking'
    list_display_links = 'title', 'caption'


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = 'title', 'caption', 'icon'
    list_display_links = 'title', 'caption'

