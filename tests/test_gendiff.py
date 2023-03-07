import pytest
import os

from gendiff.scripts.gendiff import generate_diff
from gendiff.file_parser import parse_file
from gendiff.formatters.stylish import get_normalized_value


def get_expected_result(formatter_name):
    path = 'tests/fixtures/output/'
    filename = f'{formatter_name}_expected.txt'
    path_expected = os.path.join(path, filename)
    with open(path_expected, 'r') as file:
        return file.read()


@pytest.mark.parametrize(
    "filepath1, filepath2, format_name",
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
def test_generate_diff(filepath1, filepath2, format_name):
    result = generate_diff(str(filepath1), str(filepath2), format_name)
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
