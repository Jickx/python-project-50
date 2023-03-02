import json
import yaml
import os.path


def generate_filepath(filename: str) -> str:
    """Generate filepath from filename"""
    filetype = filename.split('.')[1]
    if filetype not in ('json', 'yaml', 'yml'):
        raise TypeError('File must be json, yaml or yml.')
    if filetype == 'json':
        return os.path.join('tests', 'fixtures', 'json', filename)
    else:
        return os.path.join('tests', 'fixtures', 'yaml', filename)


def parse_file(filename: str) -> dict:
    """Get file data from filename."""
    filepath = generate_filepath(filename)
    filetype = filename.split('.')[1]
    if filetype == 'json':
        return json.load(open(filepath, 'r'))
    return yaml.safe_load((open(filepath, 'r')))
