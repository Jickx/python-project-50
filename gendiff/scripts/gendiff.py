from gendiff.file_parser import parse_file
from gendiff.cli import get_args
from gendiff.format import format_items
import json


def generate_diff(data1: dict, data2: dict) -> list:
    """Generate comparison data list of two files."""
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
            child = generate_diff(data1[key], data2[key])
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


def print_result_data_in_file(data: str) -> None:
    with open('temp.txt', 'w') as temp:
        temp.write(data)


def get_diff_str(formatted_diff: list) -> str:
    return '\n'.join(formatted_diff)


def main():
    args = get_args()
    format_name = args.format
    file1_data = parse_file(args.first_file)
    file2_data = parse_file(args.second_file)
    diff = generate_diff(file1_data, file2_data)
    formatted_diff = format_items(diff, format_name)
    if format_name == 'json':
        print(formatted_diff)
    else:
        print(get_diff_str(formatted_diff))


if __name__ == "__main__":
    main()
