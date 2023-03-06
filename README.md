# **Gendiff** - compare two json and/or yaml files
[![Actions Status](https://github.com/Jickx/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Jickx/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1ac36cb0f1f91f85effe/maintainability)](https://codeclimate.com/github/Jickx/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1ac36cb0f1f91f85effe/test_coverage)](https://codeclimate.com/github/Jickx/python-project-50/test_coverage)

## **About:**
Program generate a comparison of two json/yaml files in various formats.
- **stylish** [default]
- **plain**
- **json**

## **Setup:**
```bash
git clone https://github.com/Utrian/python-project-50
cd python-project-50
make install
```

## Help:
```bash
gendiff -h

usage: gendiff [-h] [-f [{stylish,plain,json}]] [first_file] [second_file]

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## **File samples:**
* tests/fixtures/json/file1.json
* tests/fixtures/json/file2.json
* tests/fixtures/yaml/file1.yaml
* tests/fixtures/yaml/file2.yaml

### Asciinema:
#### Step 6:
[![asciicast](https://asciinema.org/a/nBy5peYLB2VQYZwUgrvbszorA.svg)](https://asciinema.org/a/nBy5peYLB2VQYZwUgrvbszorA)
#### Step 7:
[![asciicast](https://asciinema.org/a/mtuh3UpVO93D7PDsOUnGOoJ7Y.svg)](https://asciinema.org/a/mtuh3UpVO93D7PDsOUnGOoJ7Y)
#### Step 8:
[![asciicast](https://asciinema.org/a/SgqNujzZu0Y3rla84Q1hEjvtT.svg)](https://asciinema.org/a/SgqNujzZu0Y3rla84Q1hEjvtT)
