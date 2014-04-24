from django.contrib.auth import get_user_model

from rest_framework import mixins, viewsets

from .serializers import UserCreateReadSerializer


class UserCreateReadViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateReadSerializer
