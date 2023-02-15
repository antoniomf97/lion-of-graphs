from pydantic import BaseModel
from typing import List

from pandas import DataFrame


class DataModel(BaseModel):
    plotID: int = 0
    graphID: int = 0
    limits: tuple = None
    datatype: str


class FileModel(DataModel):
    filename: str
    axis: List[str] = ['y']
    column_names: dict = {'y': 'y'}
    dataframe: DataFrame = None


class FunctionModel(DataModel):
    function: str
    resolution: int = 100
    dataframe: DataFrame = None
