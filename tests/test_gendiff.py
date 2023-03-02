from gendiff.scripts.gendiff import compare_files_data
from gendiff.file_parser import parse_file
from gendiff.format import format_items
from gendiff.formatters.stylish import get_normalized_value
from gendiff.formatters.stylish import walk_values


def get_expected_result():
    with open('tests/fixtures/output/expected.txt', 'r') as file:
        return file.read()


def test_yaml():
    yaml_file_data1 = parse_file('file1.yaml')
    yaml_file_data2 = parse_file('file2.yaml')
    yaml_comparison_data = compare_files_data(yaml_file_data1, yaml_file_data2)
    yaml_formatted_result = format_items(yaml_comparison_data)
    expected = get_expected_result()
    assert yaml_formatted_result == expected


def test_json():
    json_file_data1 = parse_file('file1.json')
    json_file_data2 = parse_file('file2.json')
    json_comparison_data = compare_files_data(json_file_data1, json_file_data2)
    json_formatted_result = format_items(json_comparison_data)
    expected = get_expected_result()
    assert json_formatted_result == expected


def test_get_normalized_value():
    value1 = None
    value2 = False
    value3 = 3
    result1 = get_normalized_value(value1)
    result2 = get_normalized_value(value2)
    result3 = get_normalized_value(value3)
    assert result1 == ' null'
    assert result2 == ' false'
    assert result3 == ' 3'


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




