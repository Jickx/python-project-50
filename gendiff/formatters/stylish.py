from gendiff.formatters.normalize import get_normalized_value

SPACES = '    '
ONE_SPACE = ' '
OPEN_CURLY_BRACKET = '{'
CLOSED_CURLY_BRACKET = '}'


def get_type(item_type: str) -> str:
    """Get proper prefix corresponding to item type."""
    item_prefix = {
        'added': '  + ',
        'deleted': '  - ',
        'unchanged': '    ',
        'nested': '    ',
    }
    return item_prefix[item_type]


def write_line(key: str, value: str,
               depth: int, item_type='unchanged') -> str:
    """Write line for corresponding key, value and type."""
    indent = SPACES * depth
    norm_value = get_normalized_value(value, 'stylish')
    return f"{indent}{get_type(item_type)}{key}:{ONE_SPACE}{norm_value}"


def walk_values(values: dict, depth: int) -> list:
    """Generate comparison output in case of multiple values."""
    result = []

    def walk(values_: dict, depth_: int) -> None:
        for k, v in values_.items():
            if isinstance(v, dict):
                result.append(write_line(k, OPEN_CURLY_BRACKET, depth_))
                walk(v, depth_ + 1)
            else:
                result.append(write_line(k, v, depth_))
        result.append(SPACES * depth_ + CLOSED_CURLY_BRACKET)
    walk(values, depth + 1)
    return result


def changed_item_format(depth, item, item_type, key, result):
    """Formatting logic for changed items."""
    value1 = item['value1']
    value2 = item['value2']
    if isinstance(value1, dict):
        result.append(write_line(key, OPEN_CURLY_BRACKET,
                                 depth, 'deleted'))
        result.extend(walk_values(value1, depth))
        result.append(write_line(key, value2, depth, 'added'))
    if isinstance(value2, dict):
        result.append(write_line(key, value1, depth, 'deleted'))
        result.append(write_line(key, OPEN_CURLY_BRACKET, depth, 'added'))
        result.extend(walk_values(value2, depth))
    elif not isinstance(value1, dict) \
            and not isinstance(value2, dict):
        result.append(write_line(key, value1, depth, 'deleted'))
        result.append(write_line(key, value2, depth, 'added'))


def added_item_format(depth, item, item_type, key, result):
    """Formatting logic for added and removed items."""
    value = item['value']
    if isinstance(value, dict):
        result.append(write_line(key, OPEN_CURLY_BRACKET,
                                 depth, item_type))
        result.extend(walk_values(value, depth))
    else:
        result.append(write_line(key, value, depth, item_type))


def nested_item_format(depth, item, item_type, key, walk, result):
    """Formatting logic for nested items."""
    children = item['children']
    result.append(write_line(key, OPEN_CURLY_BRACKET,
                             depth, item_type))
    walk(children, depth + 1)


def stylish_format(diff: list) -> list:
    """Generate comparison output via stylish formatter."""
    result = [OPEN_CURLY_BRACKET]

    def walk(tree: list, depth=0) -> None:
        for item in tree:
            item_type = item['type']
            key = item['key']

            if 'children' in item:
                nested_item_format(depth, item, item_type, key, walk, result)
            elif 'value' in item:
                added_item_format(depth, item, item_type, key, result)
            elif 'value1' in item:
                changed_item_format(depth, item, item_type, key, result)
        result.append(SPACES * depth + CLOSED_CURLY_BRACKET)

    walk(diff)
    return result
