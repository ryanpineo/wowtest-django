from django.conf.urls import patterns, include, url

from store.views import CategoryListView

urlpatterns = patterns(
    '',

    url(r'^category/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<slug>\w+)$', CategoryListView.as_view(),
        name='category-list'),
)
