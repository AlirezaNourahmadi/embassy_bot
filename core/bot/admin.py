from django.contrib import admin

from .models import ReservationRequest


@admin.register(ReservationRequest)
class ReservationRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "preferred_date", "created_at", "updated_at")
    list_filter = ("status", "preferred_date")
    search_fields = ("user__username", "user__telegram_id", "chat_id")
