from django.conf.urls import patterns, url

from store.views import CategoryListView, BreadcrumbListView

urlpatterns = patterns(
    '',

    url(r'^/categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^/categories/(?P<slug>[-\w]+)/$', CategoryListView.as_view(),
        name='category-list'),

    url(r'^/breadcrumbs/$', BreadcrumbListView.as_view(), name='breadcrumb-list'),
    url(r'^/breadcrumbs/(?P<slug>[-\w]+)/$', BreadcrumbListView.as_view(),
        name='breadcrumb-list'),
)
