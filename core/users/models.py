from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    telegram_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    chat_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.username or f"user-{self.pk}"
