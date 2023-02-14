from pydantic import BaseModel
from typing import List, Optional

from figure import Figure
from layout import Layout


class Graph(BaseModel):
    graphID: int = 0
    plots_list: List[int] = [0]


class Plot(BaseModel):
    plotID: int = 0


class Image(BaseModel):
    figure: Figure = Figure()
    layout: Layout = Layout()
    graphs: List[Graph] = [Graph()]
    plots: Optional[List[Plot]] = [Plot()]

    class Config:
        arbitrary_types_allowed = True
