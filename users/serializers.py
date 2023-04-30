from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def create(self, validated_data):
        if validated_data['is_employee'] is True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])
        instance.save()

        return instance
