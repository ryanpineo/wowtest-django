from django.conf.urls import patterns, url

from store.views import CategoriesListView, BreadcrumbsListView

urlpatterns = patterns(
    '',

    url(r'^categories/$', CategoriesListView.as_view(), name='categories-list'),
    url(r'^categories/(?P<slug>\w+)/$', CategoriesListView.as_view(),
        name='categories-list'),

    url(r'^breadcrumbs/$', BreadcrumbsListView.as_view(), name='breadcrumbs-list'),
    url(r'^breadcrumbs/(?P<slug>\w+)/$', BreadcrumbsListView.as_view(),
        name='breadcrumbs-list'),
)
