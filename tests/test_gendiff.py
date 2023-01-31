from gendiff.scripts.gendiff import generate_diff


def test_yaml():
    filename1 = 'file1.yaml'
    filename2 = 'file2.yaml'
    result = generate_diff(filename1, filename2)
    with open('tests/fixtures/output/expected.txt', 'r') as file:
        expected = file.read()
    assert result == expected


def test_json():
    filename1 = 'file1.json'
    filename2 = 'file2.json'
    result = generate_diff(filename1, filename2)
    with open('tests/fixtures/output/expected.txt', 'r') as file:
        expected = file.read()
    assert result == expected

