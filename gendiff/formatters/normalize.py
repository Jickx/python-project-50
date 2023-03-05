def check_if_complex(value):
    """If value is comples return [complex value],
    else return value with quotation."""
    return '[complex value]' if isinstance(value, dict) else f"'{value}'"


def get_normalized_value(value: any, format_name='stylish') -> str:
    """Normalize value."""
    if isinstance(value, bool):
        return 'true' if value is True else 'false'
    elif value is None:
        return 'null'
    if format_name == 'stylish':
        return str(value) if value else value
    elif format_name == 'plain':
        return check_if_complex(value) if value else "''"
