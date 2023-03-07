import pytest
import os

from gendiff.scripts.gendiff import generate_diff, get_diff_str
from gendiff.file_parser import parse_file
from gendiff.format import format_items
from gendiff.formatters.stylish import get_normalized_value
from gendiff.formatters.stylish import walk_values


def get_expected_result(formatter_name):
    path = 'tests/fixtures/output/'
    filename = f'{formatter_name}_expected.txt'
    path_expected = os.path.join(path, filename)
    with open(path_expected, 'r') as file:
        return file.read()


@pytest.mark.parametrize(
    "test_file1, test_file2, format_name",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'stylish',
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'plain',
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'plain',
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'json',
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'json',
        ),
    ],
)
def test_generate_diff(test_file1, test_file2, format_name):
    file_data1 = parse_file(str(test_file1))
    file_data2 = parse_file(str(test_file2))
    result = generate_diff(file_data1, file_data2, str(format_name))
    expected = get_expected_result(format_name)
    assert result == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(
            None,
            'null',
        ),
        pytest.param(
            False,
            'false',
        ),
        pytest.param(
            3,
            '3',
        ),
    ]
)
def test_get_normalized_value(value, expected):
    result = get_normalized_value(value)
    assert result == expected
