from rest_framework.generics import ListAPIView

from .models import Category


class CategoriesListView(ListAPIView):
    lookup_field = 'slug'
    model = Category

    def get_queryset(self):
        slug = self.kwargs.get(self.lookup_field, 'root')
        return Category.objects.filter(parent__slug=slug)


class BreadcrumbsListView(ListAPIView):
    lookup_field = 'slug'
    model = Category

    def get_queryset(self):
        slug = self.kwargs.get(self.lookup_field, 'root')
        category = Category.objects.get(slug=slug)
        return category.get_ancestors(include_self=True)
