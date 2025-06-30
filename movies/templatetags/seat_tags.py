from django import template

register = template.Library()

@register.filter
def chunk(value, chunk_size):
    """
    Splits a list into chunks of the specified size.
    Useful for rendering a grid layout in templates.
    """
    chunk_size = int(chunk_size)
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
