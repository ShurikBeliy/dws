import PIL
import os
import logging

logger = logging.getLogger(__name__)

def add_suffix_to_filename(filename, suffix):
    """ Add prefix to image filename """
    path = os.path.splitext(filename)
    path = path[:1] + (suffix,) + path[1:]
    return ''.join(path)

def change_filename_extension(filename, extension):
    """ Add prefix to image filename """
    path = os.path.splitext(filename)[:1] + (extension,)
    return '.'.join(path)

def resize_image_to_width_and_return_pil_image(image, to_width):
    """ Resize image to width. Height will change accordingly. """
    filepath = image.path
    image = PIL.Image.open(filepath)
    image = image.resize( ( to_width, round( image.height * ( to_width / image.width ) ) ) )
    return image

def convert_image_type_and_save(pil_image, image_type, image_path):
    """ Convert image to new type and save with new path """
    webp = pil_image.convert('RGB')
    webp.save(image_path,image_type)

def get_image_url_by_type(image, image_type='webp', image_width=None):
    """ Get image url. If image doesn't exists it will try to create from original """
    image_path = change_filename_extension(image.path, image_type)
    image_url = change_filename_extension(image.url, image_type)
    if image_width:
        suffix = ''.join(('_', str(image_width),))
        image_path = add_suffix_to_filename(image_path, suffix)
        image_url = add_suffix_to_filename(image_url, suffix)
    if not os.path.exists(image_path):
        pli_image = PIL.Image.open(image.path)
        if image_width:
            pli_image = resize_image_to_width_and_return_pil_image(image, image_width)
        convert_image_type_and_save(pli_image, image_type, image_path)
    return change_filename_extension(image_url, image_type)

def create_and_get_image_type_urls(image, image_type, need_retina):
    """ Generate image for retina and image that smaller 2 times if it necessary """
    try:
        retina_image = get_image_url_by_type(image, image_type, image.width )
        # if we don't need retina we will return original size image
        if not need_retina:
            return None, retina_image

        # but if we need retina we will generate image that smaller 2 time than retina image
        image = get_image_url_by_type(image, image_type, int(image.width/2) )
        return image, retina_image
    except Exception as e:
        logger.error('Exception is: {}'.format(e))
        return None, image.url
