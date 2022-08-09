import json
import jsonschema
from jsonschema.exceptions import ValidationError


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
    if not jsonschema.validate(instance=request, schema=requestSchema):
        raise ValidationError


def parse_json(request):
    """Returns a parsed JSON request"""
    return json.loads(request)


def validate_request(request):
    """Validates request json in format and schema"""
    parsed_response = parse_json(request)
    validate_schema(parsed_response)
