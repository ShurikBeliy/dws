from django.test import TestCase
from catalog.models import Item, Category
from django.db import models

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            is_active = True,
            priority = 1,
            name = "New category",
            slug = "new-category",
        )

    def test_is_active_label(self):
        obj = Category.objects.get(id=1)
        label = obj._meta.get_field('is_active').verbose_name
        self.assertEquals(label , 'Is active')
