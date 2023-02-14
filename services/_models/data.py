from pydantic import BaseModel
from typing import List


class Data(BaseModel):
    plotID: int = 0
    graphID: int = 0
    limits: tuple = None


class File(Data):
    filename: str
    axis: List[str] = ['y']
    column_names: dict = {'y': 'y'}


class Function(Data):
    function: str
    resolution: int = 100
