from gendiff.file_parser import parse_file
from gendiff.cli import get_args
from gendiff.format import format_items
from gendiff.build_aux_tree import build_aux_tree
import json


def generate_diff(filepath1: str, filepath2: str, format_name='stylish') -> str:
    """Generate comparison data list of two files."""
    file1_data = parse_file(filepath1)
    file2_data = parse_file(filepath2)
    diff = build_aux_tree(file1_data, file2_data)
    if format_name == 'json':
        return json.dumps(diff)
    formatted_diff = format_items(diff, format_name)
    return get_diff_str(formatted_diff)


def print_result_data_in_file(data: str) -> None:
    """Print data to file for debugging."""
    with open('temp.txt', 'w') as temp:
        temp.write(data)


def get_diff_str(formatted_diff: list) -> str:
    """Convert diff list result ro string."""
    return '\n'.join(formatted_diff)


def main():
    args = get_args()
    format_name = args.format
    filepath1, filepath2 = args.first_file, args.second_file
    result = generate_diff(filepath1, filepath2, format_name)
    # print_result_data_in_file(result)
    print(result)


if __name__ == "__main__":
    main()
