import json
import jsonschema
from preprocessor import preprocess_data
from fitter import fitter


requestSchema = {
    "type": "object",
    "properties": {
        "ContentB64": {"type": "string"}
    }
}


def validate_json(request):
    """Validates request JSON schema"""
    try:
        jsonschema.validate(instance=request, schema=requestSchema)
    except jsonschema.exceptions.ValidationError:
        print("Invalid request JSON schema.")
        return False
    return True


def parse_json(request):
    """Validates and parse JSON request"""
    try:
        return json.loads(request)
    except ValueError:
        print("Cannot parse request JSON.")
        exit()


def service(request):
    """Triggers the fitter engine for the given request"""
    response = None

    request = parse_json(request)
    if validate_json(request):
        data = preprocess_data(request["ContentB64"])
        response = fitter(data)

    return response.to_json().encode()
