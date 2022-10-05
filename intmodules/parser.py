from json import loads
from pandas import read_csv
from io import StringIO
from jsonschema import validate
from intmodules.exceptions import InvalidRequestError


options_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        }
    },
    "requied": []
}


def parse_request(request: tuple) -> dict:
    """Validates request json in format and schema"""

    if len(request) == 2:
        file_part, options_part = (part.content.decode(part.encoding) for part in request)
    elif len(request) == 3:
        file_part, options_part, _ = (part.content.decode(part.encoding) for part in request)
    else:
        raise InvalidRequestError

    data = read_csv(StringIO(file_part), sep=",", index_col=0)
    options = loads(options_part)

    validate(instance=options, schema=options_schema)

    return {"data": data, "options": options}
