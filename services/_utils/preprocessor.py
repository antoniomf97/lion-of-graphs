from fastapi import UploadFile
from typing import List
from pandas import DataFrame, read_csv

from .._models.data import DataModel, FileModel, FunctionModel
from .exceptions import InvalidRequestError


def validate_data(dataList: List[DataModel], rawData: UploadFile = None) -> DataFrame:
    for data in dataList:
        if data.datatype == "file":
            if rawData is None:
                raise Exception("Expected file for file datatype.")
            
            dataframe = read_csv(rawData.file, sep=',', index_col=0)[data.axis]
            dataframe = dataframe.rename(data.column_names, axis='columns')

            dataframe = validate_dataframe(dataframe=dataframe)

            data.dataframe = dataframe
        elif data.datatype == "function":
            validate_latex(data.function)
        else:
            raise Exception("Invalid File Type")


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
