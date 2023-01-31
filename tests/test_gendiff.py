from gendiff.scripts.gendiff import generate_diff


def test_gendiff():
    file1_path = 'gendiff/scripts/file1.yaml'
    file2_path = 'gendiff/scripts/file2.yaml'
    result = generate_diff(file1_path, file2_path)
    with open('gendiff/scripts/expected.txt', 'r') as file:
        expected = file.read()
    assert result == expected

