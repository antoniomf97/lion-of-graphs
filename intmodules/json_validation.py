import json
from jsonschema import validate
from intmodules.exceptions import InvalidRequestError


request_schema = {
  "type": "object",
  "properties": {
    "title": {"type": "string"}
  },
  "required": []
}


def validate_schema(request):
    """Validates request JSON schema"""
    validate(instance=request, schema=request_schema)


def parse_json(request):
    """Returns a parsed JSON request"""
    return json.loads(request)


def header_parser(headers):
    pass

def validate_content(request: tuple):
    if len(request) > 2:
        raise InvalidRequestError
    for part in request:
        part[b'Content']


def validate_request(request: tuple) -> tuple:
    """Validates request json in format and schema"""
    parsed_response = parse_json(request)
    validate_schema(parsed_response)
    return parsed_response
