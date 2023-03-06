from gendiff.scripts.gendiff import generate_diff, get_diff_str
from gendiff.file_parser import parse_file
from gendiff.format import format_items
from gendiff.formatters.stylish import get_normalized_value
from gendiff.formatters.stylish import walk_values

import os


def get_expected_result(formatter_name):
    path = 'tests/fixtures/output/'
    filename = f'{formatter_name}_expected.txt'
    path_expected = os.path.join(path, filename)
    with open(path_expected, 'r') as file:
        return file.read()


def test_yaml_stylish():
    file_data1 = parse_file('file1.yaml')
    file_data2 = parse_file('file2.yaml')
    comparison_data = generate_diff(file_data1, file_data2)
    formatted = format_items(comparison_data)
    formatted_str = get_diff_str(formatted)
    expected = get_expected_result('stylish')
    assert formatted_str == expected


def test_json_stylish():
    file_data1 = parse_file('file1.json')
    file_data2 = parse_file('file2.json')
    comparison_data = generate_diff(file_data1, file_data2)
    formatted = format_items(comparison_data)
    formatted_str = get_diff_str(formatted)
    expected = get_expected_result('stylish')
    assert formatted_str == expected


def test_json_plain():
    file_data1 = parse_file('file1.json')
    file_data2 = parse_file('file2.json')
    comparison_data = generate_diff(file_data1, file_data2)
    formatted = format_items(comparison_data, 'plain')
    formatted_str = get_diff_str(formatted)
    expected = get_expected_result('plain')
    assert formatted_str == expected


def test_yaml_plain():
    file_data1 = parse_file('file1.yaml')
    file_data2 = parse_file('file2.yaml')
    comparison_data = generate_diff(file_data1, file_data2)
    formatted = format_items(comparison_data, 'plain')
    formatted_str = get_diff_str(formatted)
    expected = get_expected_result('plain')
    assert formatted_str == expected


def test_json_json():
    file_data1 = parse_file('file1.json')
    file_data2 = parse_file('file2.json')
    comparison_data = generate_diff(file_data1, file_data2)
    formatted = format_items(comparison_data, 'json')
    expected = get_expected_result('json')
    assert formatted == expected


def test_get_normalized_value():
    value1 = None
    value2 = False
    value3 = 3
    result1 = get_normalized_value(value1)
    result2 = get_normalized_value(value2)
    result3 = get_normalized_value(value3)
    assert result1 == 'null'
    assert result2 == 'false'
    assert result3 == '3'


def test_walk_values():
    values = {'type': 'added',
              'key': 'group3',
              'value': {
                  'deep': {'id': {
                      'number': 45}},
                  'fee': 100500}}
    result = walk_values(values, depth=0)
    expected = ['        type: added',
                '        key: group3',
                '        value: {',
                '            deep: {',
                '                id: {',
                '                    number: 45',
                '                }',
                '            }',
                '            fee: 100500',
                '        }',
                '    }']
    assert result == expected