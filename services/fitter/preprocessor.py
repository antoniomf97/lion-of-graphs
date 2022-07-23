from reader import base64_to_dataframe
from validator import *


def preprocess_data(b64_data):
    """Preprocesses and validates input data"""
    data = base64_to_dataframe(b64_data)
    validate_data(data)
    return data
