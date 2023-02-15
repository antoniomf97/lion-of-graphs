from pydantic import BaseModel
from typing import List, Optional

from figure import FigureModel
from layout import LayoutModel
from plot import PlotModel


class GraphModel(BaseModel):
    graphID: int = 0
    plots_list: List[int] = [0]


class ImageModel(BaseModel):
    figure: FigureModel = FigureModel()
    layout: LayoutModel = LayoutModel()
    graphs: List[GraphModel] = [GraphModel()]
    plots: Optional[List[PlotModel]] = [PlotModel()]

    class Config:
        arbitrary_types_allowed = True
