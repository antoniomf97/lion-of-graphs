from pandas import read_csv
from fastapi import UploadFile


def parse_request(rawData: UploadFile) -> tuple:
    """Validate and parses request into dict"""

    data = read_csv(rawData.file, sep=",", index_col=0)

    return data
