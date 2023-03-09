def plain_normalized(value):
    """Normalize logic for plain style."""
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value is True else 'false'
    elif value == '0':
        return 0
    elif value is None:
        return 'null'
    elif not value:
        return "''"
    return f"'{value}'"


def stylish_normalized(value):
    """Normalize logic for stylish style."""
    if isinstance(value, bool):
        return 'true' if value is True else 'false'
    elif value == 0:
        return 0
    elif value is None:
        return 'null'
    elif value == "''":
        return "''"
    return f"{value}"


def get_normalized_value(value: str or list, format_name='stylish') -> str:
    """Normalize value."""
    if format_name == 'stylish':
        return stylish_normalized(value)
    elif format_name == 'plain':
        return plain_normalized(value)
