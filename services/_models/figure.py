from pydantic import BaseModel
from typing import Optional, Literal, Any
from matplotlib import rcParams
from matplotlib.pyplot import Figure
from matplotlib.patches import Patch
from matplotlib.path import Path
from matplotlib.transforms import Bbox, Transform
from matplotlib.patheffects import AbstractPathEffect
from matplotlib.layout_engine import LayoutEngine


"""
References:
Figure      https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure
RcParams    https://matplotlib.org/stable/tutorials/introductory/customizing.html#matplotlibrc-sample
Config      https://docs.pydantic.dev/usage/model_config/
"""


class KwargsFigureModel(BaseModel):
    # agg_filter: Optional[callable]
    alpha: Optional[float]
    animated: Optional[bool]
    canvas: Optional[Any]
    clip_box: Optional[Bbox]
    clip_on: Optional[bool]
    clip_path: Optional[Patch | tuple[Path, Transform]]
    constrained_layout: Optional[bool]
    constrained_layout_pads: Optional[Any]
    dps: Optional[float]
    edgecolor: Optional[str]
    facecolor: Optional[str]
    figheight: Optional[float]
    figure: Optional[Figure]
    figwidth: Optional[float]
    frameon: Optional[bool]
    gid: Optional[str]
    in_layout: Optional[bool]
    label: Optional[object]
    layout_engine: Optional[LayoutEngine]
    linewidth: Optional[float]
    mouseover: Optional[bool]
    path_effects: Optional[AbstractPathEffect]
    picker: Optional[bool | float | None]  # | callable
    rasterized: Optional[bool]
    size_inches: Optional[float | tuple[float, float]]
    sketch_params: Optional[tuple[float, float, float]]
    snap: Optional[bool | None]
    tight_layout: Optional[bool]
    transform: Optional[Transform]
    url: Optional[str]
    visible: Optional[bool]
    zorder: Optional[float]

    class Config:
        arbitrary_types_allowed = True


class SubplotParamsModel(BaseModel):
    # left: float = rcParams["figure.subplot.left"]
    left: float = 0.125
    right: float = 0.9
    bottom: float = 0.11
    top: float = 0.88
    wspace: float = 0.2
    hspace: float = 0.2


class FigureModel(BaseModel):
    """
    Defines the base figure configurations
    """
    figsize: tuple[float] = (6.4, 4.8)
    dpi: float = 100.0
    facecolor: str = 'white'
    edgecolor: str = 'white'
    linewidth: float = 0.0
    frameon: bool = True
    subplotpars: SubplotParamsModel = SubplotParamsModel()
    tight_layout: bool | dict = False
    constrained_layout: bool = False
    layout: Optional[Literal['constrained', 'compressed', 'tight'] | LayoutEngine | None]
    kwargs: Optional[KwargsFigureModel]

    class Config:
        arbitrary_types_allowed = True

