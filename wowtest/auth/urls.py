from django.conf.urls import patterns, url, include

from rest_framework.routers import SimpleRouter

from .views import UserCreateReadViewSet


router = SimpleRouter()
router.register(r'', UserCreateReadViewSet)

urlpatterns = patterns(
    '',

    url('', include(router.urls)),

)
