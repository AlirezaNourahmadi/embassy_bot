from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Telegram", {"fields": ("telegram_id", "chat_id")}),)
    list_display = UserAdmin.list_display + ("telegram_id", "chat_id")
    search_fields = UserAdmin.search_fields + ("telegram_id", "chat_id")
