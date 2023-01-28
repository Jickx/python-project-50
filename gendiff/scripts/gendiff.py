import argparse
import json
import os.path

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


def generate_diff(file1_path, file2_path):
    file1_json = json.load(open(file1_path, 'r'))
    file2_json = json.load(open(file2_path, 'r'))
    gen_diff = diff(file1_json, file2_json, syntax='explicit')
    sorted_keys = sorted(set(list(file1_json) + list(file2_json)))
    result = []
    for key in sorted_keys:
        if key in gen_diff[jd.delete]:
            result.append(f'- {key}: {file1_json[key]}')
        elif key in gen_diff[jd.insert]:
            result.append(f'+ {key}: {file2_json[key]}')
        elif key in gen_diff[jd.update]:
            result.append(f'- {key}: {file1_json[key]}')
            result.append(f'+ {key}: {file2_json[key]}')
        else:
            result.append(f'  {key}: {file1_json[key]}')
    return '\n'.join(result)


def gen_abs_path(path):
    os.path.abspath(path)


def main():
    args = parse_args()
    result = '\n'.join(generate_diff(args.first_file, args.second_file))
    print(result)


if __name__ == "__main__":
    main()
