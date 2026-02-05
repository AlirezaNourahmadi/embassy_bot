from django.conf import settings
from django.db import models


class ReservationRequest(models.Model):
    class Status(models.TextChoices):
        WAITING = "waiting", "Waiting"
        IN_PROGRESS = "in_progress", "In progress"
        WAITING_EMBASSY = "waiting_embassy", "Waiting for embassy response"
        FAILED = "failed", "Failed"
        DONE = "done", "Done"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservation_requests",
    )
    chat_id = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.WAITING)
    preferred_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    last_checked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.user} - {self.get_status_display()}"
