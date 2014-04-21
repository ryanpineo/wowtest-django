import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..views import CategoryListView
from . import create_categories


class CategoryListViewTests(TestCase):
    def setUp(self):
        create_categories()

    def get_categories(self, category=None):
        if category:
           response = self.client.get(reverse('category-list', args=(category,)))
        else:
            response = self.client.get(reverse('category-list'))
        return json.loads(response.content.decode('utf-8'))

    def test_base_category(self):
        """Should show the root category if no category is provided."""
        categories = self.get_categories()
        self.assertEqual(2, len(categories))

    def test_specific_category(self):
        categories = self.get_categories('weapons')
        self.assertEqual(1, len(categories))
