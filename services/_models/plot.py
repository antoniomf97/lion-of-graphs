from pydantic import BaseModel
from typing import Optional

from kwargs import KwargsLine2DModel


class PlotModel(BaseModel):
    plotID: int = 0


class BasicPlotModel(PlotModel):
    pass


class ArraysFieldsPlotModel(PlotModel):
    pass


class StastisticsPlotModel(PlotModel):
    pass


class UnstructuredCoordinatesPlotModel(PlotModel):
    pass


class Plot3DModel(PlotModel):
    pass


class LinePlotModel(BasicPlotModel):
    x: tuple | list | float
    y: tuple | list | float
    fmt: Optional[str]
    data: Optional[dict]
    scalex: bool = True
    scaley: bool = True
    kwargs: Optional[KwargsLine2DModel]
