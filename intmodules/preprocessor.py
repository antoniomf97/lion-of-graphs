from intmodules.reader import base64_to_dataframe
from intmodules.validator import validate_data


def preprocess_data(b64_data):
    """Decodes, converts and validates input data"""
    data = base64_to_dataframe(b64_data)
    validate_data(data)
    return data