from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^store/', include('store.urls')),
    url(r'^users', include('auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
