from pydantic import BaseModel
from typing import Optional, Callable, Literal

from matplotlib.patches import Patch
from matplotlib.path import Path
from matplotlib.pyplot import Figure
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Bbox, Transform
from matplotlib._enums import CapStyle, JoinStyle
from matplotlib.patheffects import AbstractPathEffect


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


class KwargsLine2DModel(BaseModel):
    agg_filter: Optional[Callable]
    alpha: Optional[float]
    animated: Optional[bool]
    antialiased: Optional[bool]
    clip_box: Optional[Bbox]
    clip_on: Optional[bool]
    clip_path: Optional[Patch | tuple[Path, Transform]]
    color: Optional[str]
    dash_capstyle: Optional[Literal['butt', 'projecting', 'round'] | CapStyle]
    dash_joinstyle: Optional[Literal['miter', 'round', 'bevel'] | JoinStyle]
    dashes: Optional[tuple[float] | tuple[None, None]]   
    data: Optional[dict]
    drawstyle: Optional[Literal['default', 'steps', 'steps-pre', 'steps-mid', 'steps-post']]
    figure: Optional[Figure]
    fillstyle: Optional[Literal['full', 'left', 'right', 'bottom', 'top', 'none']]
    gapcolor: Optional[str]
    gid: Optional[str]
    in_layout: Optional[bool]
    label: Optional[object]
    linestyle | ls: Optional[str | tuple[float, tuple]]
    linewidth | lw: Optional[float]
    marker: Optional[str | Path | MarkerStyle]
    markeredgecolor | mec: Optional[str]
    markeredgewidth | mew: Optional[float]
    markerfacecolor | mfc: Optional[str]
    markerfacecoloralt | mfcalt: Optional[str]
    markersize | ms: Optional[float]
    markevery: Optional[None | int | tuple[int, int] | list[int] | float | tuple[float, float] | list[bool]]
    mouseover: Optional[bool]
    path_effects: Optional[AbstractPathEffect]
    picker: Optional[bool | float | Callable | None]
    pickradius: Optional[float]
    rasterized: Optional[bool]
    sketch_params: Optional[tuple[float, float, float]]
    snap: Optional[bool | None]
    solid_capstyle: Optional[Literal['butt', 'projecting', 'round'] | CapStyle]
    solid_joinstyle: Optional[Literal['miter', 'round', 'bevel'] | JoinStyle]
    transform: Optional[Transform]
    url: Optional[str]
    visible: Optional[bool]
    xdata: Optional[list[float]]
    ydata: Optional[list[float]]
    zorder: Optional[float]


class LinePlotModel(BasicPlotModel):
    x: tuple | float
    y: tuple | float
    fmt: Optional[str]
    data: Optional[dict]
    scalex: bool = True
    scaley: bool = True
    kwargs: Optional[KwargsLine2DModel]
