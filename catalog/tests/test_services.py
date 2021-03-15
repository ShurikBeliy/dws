from django.test import TestCase
from catalog.services.category import *

class CategoryServiceTest(TestCase):

    category = None
    items = None
    slug = None

    @classmethod
    def setUpTestData(cls):
        cls.slug = "new-category4"

        cls.category = Category.objects.create(
            is_active = True,
            priority = 1,
            name = "New category",
            slug = cls.slug,
        )

        Item.objects.create(
            is_active = True,
            priority = 1,
            name = "New item",
            slug = "new-item4",
            category = cls.category,
            description = "Test description"
        )

        Characteristic.objects.create(
            is_active = True,
            priority = 1,
            name = 'Characteristic1',
            category = cls.category
        )

        cls.items = Item.objects.filter(is_active=True, category_id=cls.category.id)
        cls.categories = Category.objects.filter(is_active=True)
        cls.filters = Characteristic.objects.filter(is_active=True, category_id=cls.category.id)

    def test_get_category_active_data_service_value(self):
        value = get_active_category_data(self.slug)
        self.assertEqual(value['category'], self.category)
        self.assertQuerysetEqual(value['items'], self.items, transform=lambda x: x)

    def test_get_active_category_by_slug_value(self):
        value = get_active_category_by_slug(self.slug)
        self.assertEqual(value, self.category)

    def test_get_active_items_by_category_id_value(self):
        value = get_active_items_by_category_id(self.category.id)
        self.assertQuerysetEqual(value, self.items, transform=lambda x: x)

    def test_get_active_categories_value(self):
        value = get_active_categories()
        self.assertQuerysetEqual(value, self.categories, transform=lambda x: x)

    def test_get_filter_by_category_id_value(self):
        value = get_filter_by_category_id(self.category.id)
        self.assertQuerysetEqual(value, self.filters, transform=lambda x: x)
