from django.test import TestCase
from django.urls import reverse
from catalog.models import Category

class CategoryDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(
            is_active = True,
            priority = 1,
            name = "New category",
            slug = "new-category3",
        )

    def test_category_detail_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/catalog/new-category3/')
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_url_accessible_by_name_and_slug(self) -> None:
        response = self.client.get(reverse('category_detail_url', kwargs={'slug': 'new-category3'}))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_uses_correct_template(self) -> None:
        response = self.client.get('/catalog/new-category3/')
        self.assertTemplateUsed(response, 'catalog/category.html')
