import json
import jsonschema
from jsonschema.exceptions import ValidationError
from preprocessor import preprocess_data
from fitter import fitter


requestSchema = {
  "type": "object",
  "properties": {
    "Filename": {"type": "string"},
    "ContentB64": {"type": "string"}
  },
  "required": ["Filename", "ContentB64"]
}


def validate_json(request):
    """Validates request JSON schema"""
    try:
        jsonschema.validate(instance=request, schema=requestSchema)
        return True
    except ValidationError as err:
        print("Invalid request JSON schema.")
        exit()
        return False


def parse_json(request):
    """Validates and parse JSON request"""
    try:
        return json.loads(request)
    except ValueError:
        print("Invalid request: cannot parse JSON.")
        exit()


def service(request):
    """Triggers the fitter engine for the given request"""
    response = None

    request = parse_json(request)
    if validate_json(request):
        data = preprocess_data(request["ContentB64"])
        fitter(data)
        response = data

    return data.to_json().encode()
