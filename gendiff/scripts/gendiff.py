from gendiff.file_parser import parse_file
from gendiff.cli import get_args
import jsondiff as jd
from jsondiff import diff


def generate_diff(file1_path, file2_path):
    """Generate string with differences of two files"""
    file1_data = parse_file(file1_path)
    file2_data = parse_file(file2_path)
    gen_diff = diff(file1_data, file2_data, syntax='explicit')
    keys = list(file1_data) + list(file2_data)
    sorted_keys = sorted(set(keys))
    result = []
    for key in sorted_keys:
        if key in gen_diff[jd.delete]:
            result.append(f'- {key}: {file1_data[key]}')
        elif key in gen_diff[jd.insert]:
            result.append(f'+ {key}: {file2_data[key]}')
        elif key in gen_diff[jd.update]:
            result.append(f'- {key}: {file1_data[key]}')
            result.append(f'+ {key}: {file2_data[key]}')
        else:
            result.append(f'  {key}: {file1_data[key]}')
    return '\n'.join(result)


def main():
    args = get_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
