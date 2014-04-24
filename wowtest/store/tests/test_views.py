import json

from django.core.urlresolvers import reverse
from django.test import TestCase

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

    def test_hyphen_in_category_name(self):
        categories = self.get_categories('two-handed-swords')
        self.assertEqual(0, len(categories))


class BreadcrumbListViewTests(TestCase):
    def setUp(self):
        create_categories()

    def get_breadcrumbs(self, category=None):
        if category:
            response = self.client.get(reverse('breadcrumb-list',
                                               args=(category,)))
        else:
            response = self.client.get(reverse('breadcrumb-list'))
        return json.loads(response.content.decode('utf-8'))

    def test_base_category(self):
        """Should contain only the root category if no category is provided."""
        breadcrumbs = self.get_breadcrumbs()
        self.assertEqual(1, len(breadcrumbs))

    def test_specific_category(self):
        breadcrumbs = self.get_breadcrumbs('mail')
        self.assertEqual(3, len(breadcrumbs))
        self.assertEqual('Armor', breadcrumbs[1]['name'])

    def test_hypen_in_category_name(self):
        breadcrumbs = self.get_breadcrumbs('two-handed-swords')
        self.assertEqual(4, len(breadcrumbs))
        self.assertEqual('Two Handed Swords', breadcrumbs[-1]['name'])
