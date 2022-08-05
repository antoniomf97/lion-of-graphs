import json
import jsonschema
from jsonschema.exceptions import ValidationError
from intmodules import logger, InvalidJsonFormatError, InvalidJsonSchemaError


requestSchema = {
  "type": "object",
  "properties": {
    "Filename": {"type": "string"},
    "ContentB64": {"type": "string"}
  },
  "required": ["Filename", "ContentB64"]
}


def validate_schema(request):
    """Validates request JSON schema"""
    try:
        jsonschema.validate(instance=request, schema=requestSchema)
    except ValidationError as err:
        logger.error(f"{err}: Invalid request JSON schema.")
        raise InvalidJsonSchemaError
    else:
        return True


def parse_json(request):
    """Validates and parse JSON request"""
    try:
        return json.loads(request)
    except ValueError as err:
        logger.error(f"{err}: Invalid request: cannot parse JSON.")
        raise InvalidJsonFormatError


def validate_request(request):
    """Validates request json in format and schema"""
    parsed_response = parse_json(request)
    if validate_schema(parsed_response):
        return parsed_response
    else:
        logger.error("Invalid request. Service was abandoned.")
        raise
