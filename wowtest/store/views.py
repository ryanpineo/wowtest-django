from rest_framework.generics import ListAPIView

from .models import Category


class CategoryListView(ListAPIView):
    lookup_field = 'slug'
    model = Category

    def get_queryset(self):
        slug = self.kwargs.get('slug', 'root')
        return Category.objects.filter(parent__slug=slug)
