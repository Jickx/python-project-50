import argparse
import json

import jsondiff as jd
from jsondiff import diff


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def generate_difference(file1_json, file2_json) -> list:
    get_diff = diff(file1_json, file2_json, syntax='explicit')
    sorted_keys = sorted(set(list(file1_json) + list(file2_json)))
    result = []
    for key in sorted_keys:
        if key in get_diff[jd.delete]:
            result.append(f'- {key}: {file1_json[key]}')
        elif key in get_diff[jd.insert]:
            result.append(f'+ {key}: {file2_json[key]}')
        elif key in get_diff[jd.update]:
            result.append(f'- {key}: {file1_json[key]}')
            result.append(f'+ {key}: {file2_json[key]}')
        else:
            result.append(f'  {key}: {file1_json[key]}')
    return result


def collect_json_from_file(file_path):
    return json.load(open(file_path, 'r'))


def main():
    args = parse_args()
    file1_json, file2_json = (
        collect_json_from_file(args.first_file),
        collect_json_from_file(args.second_file)
    )

    result = generate_difference(file1_json, file2_json)
    for line in result:
        print(line)


if __name__ == "__main__":
    main()
