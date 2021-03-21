from django.utils.html import format_html

class ItemAdminMixin:
    """ Additional functional for ItemAdmin """
    def category_column(self, obj) -> str:
        if obj.category :
            return format_html('<span>{}</stan>', obj.category.name)
        return format_html('<span>{}</stan>', '-')
    category_column.short_description = 'Category'

