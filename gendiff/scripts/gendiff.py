from gendiff.file_parser import parse_file
from gendiff.cli import get_args
from gendiff.format import format_items
from gendiff.build_aux_tree import build_aux_tree


def generate_diff(file1_data: dict, file2_data: dict, format_name: str):
    """Generate comparison data list of two files."""
    diff = build_aux_tree(file1_data, file2_data)
    formatted_diff = format_items(diff, format_name)
    if format_name == 'json':
        return formatted_diff
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
    file1_data = parse_file(args.first_file)
    file2_data = parse_file(args.second_file)
    print(generate_diff(file1_data, file2_data, format_name))


if __name__ == "__main__":
    main()
