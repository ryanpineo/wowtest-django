from django.contrib.auth import get_user_model
from django.core import validators
from django.utils.text import slugify

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        validators=[validators.MaxLengthValidator(16)], write_only=True)
    slug = serializers.CharField(read_only=True)


class UserCreateReadSerializer(UserSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'slug')
        read_only_fields = ('id',)

    def restore_object(self, attrs, instance=None):
        User = get_user_model()
        user = User(username=attrs['username'], email=attrs['email'])
        user.set_password(attrs['password'])
        return user
