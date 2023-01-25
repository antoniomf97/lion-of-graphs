from pandas import DataFrame

from .exceptions import InvalidRequestError


def validate_dataframe(dataframe: DataFrame) -> DataFrame:
    """Validates input data"""
    data_nulls = dataframe.isnull()
    if data_nulls.any().any():
        raise InvalidRequestError("found NaN value in provided data")

    for col in dataframe.columns:
        dataframe[col] = dataframe[col].astype(float)

    index = dataframe.index.values
    if not len(index) == len(set(index)):
        raise InvalidRequestError("found duplicated entry in provided data")

    return dataframe


def validate_latex(function: str) -> str:
    return function

