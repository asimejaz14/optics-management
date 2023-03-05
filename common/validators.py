from rest_framework.exceptions import ValidationError


def validate_image(image_obj):
    """

    Args:
        image_obj: uploaded image file

    Returns:
        object: returns true if condition matches otherwise raises validation exception
    """
    filesize = image_obj.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max image size is {megabyte_limit}MB")