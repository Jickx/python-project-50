def build_aux_tree(data1: dict, data2: dict) -> list:
    """Generate auxilary tree with differences."""
    all_keys = sorted(set(data1) | set(data2))
    diff = []

    for key in all_keys:
        if key not in data2:
            diff.append({
                'type': 'deleted',
                'key': key,
                'value': data1[key],
            })
        elif key not in data1:
            diff.append({
                'type': 'added',
                'key': key,
                'value': data2[key],
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child = build_aux_tree(data1[key], data2[key])
            diff.append({
                'type': 'nested',
                'key': key,
                'children': child,
            })
        elif data1[key] != data2[key]:
            diff.append({
                'type': 'changed',
                'key': key,
                'value1': data1[key],
                'value2': data2[key],
            })
        else:
            diff.append({
                'type': 'unchanged',
                'key': key,
                'value': data1[key],
            })

    return diff
