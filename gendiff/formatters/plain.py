from gendiff.formatters.normalize import get_normalized_value


def write_line(prop: list, value: str or list, item_type: str) -> str:
    prop_str = '.'.join(prop)
    norm_value = get_normalized_value(value, 'plain')
    if item_type == 'added':
        return f"Property '{prop_str}' was added with value: {norm_value}"
    elif item_type == 'deleted':
        return f"Property '{prop_str}' was removed"
    elif item_type == 'changed':
        norm_values = [get_normalized_value(x, 'plain') for x in value]
        return (f"Property '{prop_str}' was updated. "
                f"From {norm_values[0]} to {norm_values[1]}")


def plain_format(diff: list) -> list:
    result = []

    def walk(tree: list, prop: list) -> None:
        for item in tree:
            prop.append(item['key'])
            item_type = item['type']
            if 'children' in item:
                walk(item['children'], prop)
            elif item_type == 'added' or item_type == 'deleted':
                value = item['value']
                line = write_line(prop, value, item_type)
                result.append(line)
            elif item_type == 'changed':
                value = [(item['value1']), (item['value2'])]
                line = write_line(prop, value, item_type)
                result.append(line)
            prop.pop()

    walk(diff, prop=[])
    return result
