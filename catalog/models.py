from django.db import models


class Category(models.Model):
    """ Caegories of items """
    is_active = models.BooleanField('Is active', default=False, db_index=True)
    priority = models.PositiveIntegerField('Priority')
    name = models.CharField('Category name', max_length=150)
    slug = models.SlugField('Slug', max_length=50, allow_unicode=True, db_index=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('priority',)

class Item(models.Model):
    """ Items """
    is_active = models.BooleanField('Is active', default=False, db_index=True)
    priority = models.PositiveIntegerField('Priority')
    name = models.CharField('Item', max_length=150)
    slug = models.SlugField('Slug', max_length=50, allow_unicode=True, db_index=True)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('priority',)
