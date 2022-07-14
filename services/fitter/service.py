import json
from preprocessor import plotter


def validate_json(request):
    pass


def service(request):
    validate_json(request)
    parsed = json.loads(request)
    response = plotter(parsed["filename"]).to_json().encode()

    return response

