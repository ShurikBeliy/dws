from django.test import TestCase
from catalog.models import Item, Category

class CategoryModelTest(TestCase):

    obj = None

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            is_active = True,
            priority = 1,
            name = "New category",
            slug = "new-category",
        )
        cls.obj = Category.objects.get(id=1)

    def test_is_active_label_value(self):
        label = self.obj._meta.get_field('is_active').verbose_name
        self.assertEquals(label , 'Is active')

    def test_is_active_default_value(self):
        value = self.obj._meta.get_field('is_active').default
        self.assertFalse(value)

    def test_is_active_db_index_value(self):
        value = self.obj._meta.get_field('is_active').db_index
        self.assertTrue(value)


    def test_priority_label_value(self):
        label = self.obj._meta.get_field('priority').verbose_name
        self.assertEquals(label , 'Priority')


    def test_name_label_value(self):
        label = self.obj._meta.get_field('name').verbose_name
        self.assertEquals(label , 'Category name')

    def test_name_max_length_value(self):
        max_length = self.obj._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)


    def test_slug_label_value(self):
        label = self.obj._meta.get_field('slug').verbose_name
        self.assertEquals(label , 'Slug')

    def test_slug_max_length_value(self):
        max_length = self.obj._meta.get_field('slug').max_length
        self.assertEquals(max_length, 50)

    def test_slug_allow_unicode_value(self):
        value = self.obj._meta.get_field('slug').allow_unicode
        self.assertTrue(value)



    def test_category_model_verbose_name_value(self):
        verbose_name = self.obj._meta.verbose_name
        self.assertEquals(verbose_name , 'Category')

    def test_categoy_model_verbose_name_plural_value(self):
        verbose_name_plural = self.obj._meta.verbose_name_plural
        self.assertEquals(verbose_name_plural , 'Categories')

    def test_categoy_model_ordering_value(self):
        ordering = self.obj._meta.ordering
        self.assertEquals(ordering , ('priority',))

    def test_category_str_method_return_string_that_equal_name_field(self):
        self.assertEquals(str(self.obj), str(self.obj.name))






class ItemModelTest(TestCase):

    obj = None

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            is_active = True,
            priority = 2,
            name = "New category2",
            slug = "new-category2",
        )

        Item.objects.create(
            is_active = True,
            priority = 1,
            name = "New item",
            slug = "new-item",
            category = category,
            description = "Test description"
        )
        cls.obj = Item.objects.get(id=1)

    def test_is_active_label_value(self):
        label = self.obj._meta.get_field('is_active').verbose_name
        self.assertEquals(label , 'Is active')

    def test_is_active_default_value(self):
        value = self.obj._meta.get_field('is_active').default
        self.assertFalse(value)

    def test_is_active_db_index_value(self):
        value = self.obj._meta.get_field('is_active').db_index
        self.assertTrue(value)


    def test_priority_label_value(self):
        label = self.obj._meta.get_field('priority').verbose_name
        self.assertEquals(label , 'Priority')


    def test_name_label_value(self):
        label = self.obj._meta.get_field('name').verbose_name
        self.assertEquals(label , 'Item')

    def test_name_max_length_value(self):
        max_length = self.obj._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)


    def test_slug_label_value(self):
        label = self.obj._meta.get_field('slug').verbose_name
        self.assertEquals(label , 'Slug')

    def test_slug_max_length_value(self):
        max_length = self.obj._meta.get_field('slug').max_length
        self.assertEquals(max_length, 50)

    def test_slug_allow_unicode_value(self):
        value = self.obj._meta.get_field('slug').allow_unicode
        self.assertTrue(value)


    def test_category_related_model(self):
        related_model = self.obj._meta.get_field('category').related_model
        self.assertEquals(related_model, Category)

    def test_category_label_value(self):
        value = self.obj._meta.get_field('category').verbose_name
        self.assertEquals(value , 'Category')

    def test_category_related_name_value(self):
        value = self.obj._meta.get_field('category').related_query_name()
        self.assertEquals(value , 'items')

    def test_category_null_value(self):
        value = self.obj._meta.get_field('category').null
        self.assertTrue(value)


    def test_description_lable_value(self):
        value = self.obj._meta.get_field('description').verbose_name
        self.assertEquals(value , 'Description')

    def test_description_blank_value(self):
        value = self.obj._meta.get_field('description').blank
        self.assertTrue(value)



    def test_item_model_verbose_name_value(self):
        verbose_name = self.obj._meta.verbose_name
        self.assertEquals(verbose_name , 'Item')

    def test_item_model_verbose_name_plural_value(self):
        verbose_name_plural = self.obj._meta.verbose_name_plural
        self.assertEquals(verbose_name_plural , 'Items')

    def test_item_model_ordering_value(self):
        ordering = self.obj._meta.ordering
        self.assertEquals(ordering , ('priority',))

    def test_item_str_method_return_string_that_equal_name_field(self):
        self.assertEquals(str(self.obj), str(self.obj.name))
