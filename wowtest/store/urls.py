from django.conf.urls import patterns, include, url

from store.views import CategoryListView, BreadcrumbListView

urlpatterns = patterns(
    '',

    url(r'^category/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<slug>\w+)/$', CategoryListView.as_view(),
        name='category-list'),

    url(r'^breadcrumb/$', BreadcrumbListView.as_view(), name='breadcrumb-list'),
    url(r'^breadcrumb/(?P<slug>\w+)/$', BreadcrumbListView.as_view(),
        name='breadcrumb-list'),
)
