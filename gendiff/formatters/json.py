import json


def json_format(diff: list) -> json:
    json_diff = json.dumps(diff[0])
    return json_diff
