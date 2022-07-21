from ext_modules.reader import base64_to_dataframe
from ext_modules.validator import validate_data


def preprocess_data(b64_data):
    """Decodes, converts and validates input data"""
    data = base64_to_dataframe(b64_data)
    validate_data(data)
    return data
