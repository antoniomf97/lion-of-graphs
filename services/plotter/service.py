import json
from preprocessor import plotter


def validate_json(request):
    pass


def service(request):
    validate_json(request)

    parsed = json.loads(request)

    response = None

    if parsed["engine"] == "plotter":
        response = plotter(parsed["filename"]).to_json().encode()
    elif parsed["engine"] == "fitter":
        # response = fitter(parsed["filename"]).to_json().encode()
        response = "'cenas':'cenas'".encode()

    return response

