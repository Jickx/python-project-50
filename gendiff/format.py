from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format


def format_items(diff: list, format_name='stylish') -> list:
    formatters_types = {
        'stylish': stylish_format,
        'plain': plain_format,
    }
    formatter = formatters_types[format_name]
    return formatter(diff)
