from django import template
from catalog.services.utils import create_and_get_image_type_urls

register = template.Library()

@register.simple_tag()
def get_webp_srcset(image, need_retina=False) -> str:
    """ Create webp and return urls """
    return get_image_type_srcset(image, 'webp', need_retina)

@register.simple_tag()
def get_jpeg_srcset(image, need_retina=False) -> str:
    """ Create jpeg and return urls """
    return get_image_type_srcset(image, 'jpeg', need_retina)

@register.simple_tag()
def get_png_srcset(image, need_retina=False) -> str:
    """ Create png and return urls """
    return get_image_type_srcset(image, 'png', need_retina)

def get_image_type_srcset(image, image_type='webp', need_retina=False) -> str:
    """ Create image if it necessary and return url 
        use need retina to have small image(2 times smaller) 
        for usual monitors and normal image for retina """
    image2x, image1x = create_and_get_image_type_urls(image, image_type, need_retina)
    if image2x:
        return '%s 2x, %s 1x' % (image2x, image1x)
    return '%s 1x' % (image1x)
