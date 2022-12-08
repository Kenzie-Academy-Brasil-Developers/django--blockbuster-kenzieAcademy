from rest_framework import serializers
from .models import User
from datetime import datetime


class UserSerializer(serializers.Serializer):
    """
    Validação referente a (class) models.User
    """

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    birthdate = serializers.DateField(default=datetime.now)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def validate_email(self, email: str) -> str:
        email_already_exists = User.objects.filter(email=email).exists()

        if email_already_exists:
            raise serializers.ValidationError(detail="email already registered.")

        return email

    def validate_username(self, username: str) -> str:
        username_already_exists = User.objects.filter(username=username).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already taken.")

        return username
