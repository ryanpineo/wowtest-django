from django.core import validators
from django.utils.text import slugify

from rest_framework import serializers

from .models import Account


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        validators=[validators.MaxLengthValidator(16)], write_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Account


class UserCreateReadSerializer(UserSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'password', 'slug')
        read_only_fields = ('id',)

    def restore_object(self, attrs, instance=None):
        User = Account
        user = User(username=attrs['username'], email=attrs['email'])
        user.set_password(attrs['password'])
        return user
