from io import StringIO
from json import loads

from jsonschema import validate
from pandas import read_csv

from utils.exceptions import InvalidRequestError

options_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        }
    },
    "requied": []
}


def parse_request(request: tuple) -> tuple:
    """Validate and parses request into dict"""

    if len(request) == 3:
        file_part, options_part, func_part = (part for part in request)
    else:
        raise InvalidRequestError("Expected three parts in multipart/form-data submit.")

    data = read_csv(StringIO(file_part), sep=",", index_col=0)
    options = loads(options_part)

    validate(instance=options, schema=options_schema)

    return data, options, func_part
