from pydantic import BaseModel
from typing import List, Callable

from pandas import DataFrame


class DataModel(BaseModel):
    datatype: str
    plotID: int = 0
    graphID: int = 0
    limits: tuple = None
    dataframe: DataFrame = None

    class Config:
        arbitrary_types_allowed = True


class FileModel(DataModel):
    filename: str
    axis: List[str] = ["y"]
    column_names: dict = {"y": "y"}
    

class FunctionModel(DataModel):
    function: str
    resolution: int = 100
    lambda_f: Callable = None
