from rest_framework import mixins, viewsets

from .serializers import UserCreateReadSerializer
from .models import Account


class UserCreateReadViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = UserCreateReadSerializer
