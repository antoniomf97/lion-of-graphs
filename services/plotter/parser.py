from io import StringIO
from json import loads

from jsonschema import validate
from pandas import read_csv

from utils.exceptions import InvalidRequestError


def parse_request(request: tuple, options_schema: dict) -> dict:
    """Validate and parses request into dict"""

    if len(request) == 2:
        file_part, options_part = (part.content.decode(part.encoding) for part in request)
    else:
        raise InvalidRequestError("Expected two parts in multipart/form-data submit.")

    data = read_csv(StringIO(file_part), sep=",", index_col=0)
    options = loads(options_part)

    validate(instance=options, schema=options_schema)

    return {"data": data, "options": options}
