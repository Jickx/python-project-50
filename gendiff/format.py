from gendiff.formatters.stylish import stylish_format


def format_items(diff: list, formatter_name='stylish') -> str:
    formatters_types = {
        'stylish': stylish_format,
    }
    formatter = formatters_types[formatter_name]
    return formatter(diff)
