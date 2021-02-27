from django.db import models


class Category(models.Model):
    """ Categories of items """
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
    preview = models.ImageField('Preview', upload_to='item_preview/', blank=True)
    category = models.ForeignKey('category', verbose_name='Category', on_delete=models.CASCADE, related_name='items', null=True)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('priority',)

class ItemImage(models.Model):
    """ Images for item """
    is_active = models.BooleanField('Is active', default=False, db_index=True)
    priority = models.PositiveIntegerField('Priority')
    item = models.ForeignKey('item', verbose_name='Item', on_delete=models.CASCADE, related_name='images', null=True)
    alt = models.CharField('Alt', max_length=150)
    image = models.ImageField('Image', upload_to='item_image/', blank=True)

    def __str__(self):
        return '%s' % (self.alt)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('priority',)
