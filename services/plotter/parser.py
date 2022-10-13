from json import loads, load
from pandas import read_csv
from io import StringIO
from jsonschema import validate
from services.utils import InvalidRequestError


def parse_request(request: tuple) -> dict:
    """Validate and parses request into dict"""

    if len(request) == 2:
        file_part, options_part = (part.content.decode(part.encoding) for part in request)
    else:
        raise InvalidRequestError("Expected two parts in multipart/form-data submit.")

    data = read_csv(StringIO(file_part), sep=",", index_col=0)
    options = loads(options_part)

    with open(".\services\plotter\schema.json") as f:
        options_schema = load(f)
    validate(instance=options, schema=options_schema)

    return {"data": data, "options": options}
