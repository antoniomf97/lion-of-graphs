from pydantic import BaseModel
from typing import List, Optional

from figure import Figure


class Layout(BaseModel):
    pass


class Graph(BaseModel):
    graphID: int
    plots_list: List[int]


class Plot(BaseModel):
    plotID: int


class Image(BaseModel):
    figure: Figure = Figure()
    layout: Layout = Layout()
    graphs: List[Graph] = List[Graph()]
    plots: Optional[List[Plot]] = List[Plot()]

    class Config:
        arbitrary_types_allowed = True
