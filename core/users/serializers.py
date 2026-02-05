from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "telegram_id",
            "chat_id",
            "date_joined",
            "is_active",
        ]
        read_only_fields = ["id", "date_joined", "is_active"]
