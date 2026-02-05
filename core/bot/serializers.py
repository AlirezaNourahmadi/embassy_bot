from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ReservationRequest


User = get_user_model()


class ReservationRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ReservationRequest
        fields = [
            "id",
            "user",
            "chat_id",
            "status",
            "preferred_date",
            "notes",
            "last_checked_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "last_checked_at"]
