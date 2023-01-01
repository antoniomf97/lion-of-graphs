from io import BytesIO
from json import loads

from jsonschema import validate
from pandas import read_csv

from utils.exceptions import InvalidRequestError


def parse_request(rawData: bytes, rawOptions: str, options_schema: dict) -> tuple:
    """Validate and parses request into dict"""

    if rawData is None or rawOptions is None:
        raise InvalidRequestError("Expected two parts in multipart/form-data submit.")

    data = read_csv(BytesIO(rawData), sep=",", index_col=0)
    options = loads(rawOptions)

    validate(instance=options, schema=options_schema)

    return data, options
