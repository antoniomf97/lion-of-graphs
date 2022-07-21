import base64
import binascii
import pandas as pd
from io import StringIO


def base64_to_string(b64_data):
    """Decodes base64 encoded data to string with utf-8 encoding"""
    try:
        return base64.b64decode(b64_data).decode('utf-8')
    except binascii.Error:
        print("Invalid base64 encoding.")
        exit()
    except UnicodeDecodeError:
        print("Invalid character utf-8 encoding.")
        exit()


def string_to_dataframe(string_data):
    """Defines pandas dataframe from decoded data"""
    try:
        return pd.read_csv(StringIO(string_data), sep=",", index_col=0)
    except ValueError:
        print("Unable to read data as csv: invalid data format.")
        exit()


def base64_to_dataframe(b64_data):
    """Converts base64 data to pandas dataframe"""
    return string_to_dataframe(base64_to_string(b64_data))

