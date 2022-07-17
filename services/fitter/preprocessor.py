from reader import base64_to_dataframe
from validator import *


def preprocess_data(b64_data):
    """Validates input data"""
    data = base64_to_dataframe(b64_data)
    # <-- validator here
    validate_data(data)
    return data
