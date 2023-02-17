from pydantic import BaseModel
from typing import Optional, Callable, Literal, Any, List

from matplotlib.patches import Patch
from matplotlib.colors import Colormap, Normalize
from matplotlib.path import Path
from matplotlib.pyplot import Figure
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Bbox, Transform, IdentityTransform
from matplotlib._enums import CapStyle, JoinStyle
from matplotlib.patheffects import AbstractPathEffect
from matplotlib.layout_engine import LayoutEngine


class KwargsModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class KwargsFigureModel(KwargsModel):
    agg_filter: Optional[Callable]
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
    picker: Optional[bool | float | Callable | None]
    rasterized: Optional[bool]
    size_inches: Optional[float | tuple[float, float]]
    sketch_params: Optional[tuple[float, float, float]]
    snap: Optional[bool | None]
    tight_layout: Optional[bool]
    transform: Optional[Transform]
    url: Optional[str]
    visible: Optional[bool]
    zorder: Optional[float]


class KwargsLine2DModel(KwargsModel):
    agg_filter: Optional[Callable]
    alpha: Optional[float]
    animated: Optional[bool]
    antialiased: Optional[bool]
    clip_box: Optional[Bbox]
    clip_on: Optional[bool]
    clip_path: Optional[Patch | tuple[Path, Transform]]
    color: Optional[str]
    dash_capstyle: Optional[Literal["butt", "projecting", "round"] | CapStyle]
    dash_joinstyle: Optional[Literal["miter", "round", "bevel"] | JoinStyle]
    dashes: Optional[tuple[float] | tuple[None]]
    data: Optional[dict]
    drawstyle: Optional[
        Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"]
    ]
    figure: Optional[Figure]
    fillstyle: Optional[Literal["full", "left", "right", "bottom", "top", "none"]]
    gapcolor: Optional[str]
    gid: Optional[str]
    in_layout: Optional[bool]
    label: Optional[object]
    linestyle: Optional[str | tuple[float, tuple]]
    linewidth: Optional[float]
    marker: Optional[str | Path | MarkerStyle]
    markeredgecolor: Optional[str]
    markeredgewidth: Optional[float]
    markerfacecolor: Optional[str]
    markerfacecoloralt: Optional[str]
    markersize: Optional[float]
    markevery: Optional[
        None
        | int
        | tuple[int, int]
        | list[int]
        | float
        | tuple[float, float]
        | list[bool]
    ]
    mouseover: Optional[bool]
    path_effects: Optional[AbstractPathEffect]
    picker: Optional[bool | float | Callable | None]
    pickradius: Optional[float]
    rasterized: Optional[bool]
    sketch_params: Optional[tuple[float, float, float]]
    snap: Optional[bool | None]
    solid_capstyle: Optional[Literal["butt", "projecting", "round"] | CapStyle]
    solid_joinstyle: Optional[Literal["miter", "round", "bevel"] | JoinStyle]
    transform: Optional[Transform]
    url: Optional[str]
    visible: Optional[bool]
    xdata: Optional[list[float]]
    ydata: Optional[list[float]]
    zorder: Optional[float]


class KwargsCollectionModel(KwargsModel):
    edgecolor: str | List[str] = "black"
    facecolor: str | List[str] = "C0"
    linewidths: float | List[float] = 1.0
    linestyles: str | List[str] = "solid"
    capstyle: CapStyle = "butt"
    joinstyle: JoinStyle = "miter"
    antialiaseds: bool | List[bool] = True
    offsets: tuple[float, float] | list = (0, 0)
    offset_transform: Transform = IdentityTransform
    cmap: str | Colormap = "viridis"
    norm: Optional[str | Normalize]
    hatch: Optional[str]
    pickradius: float = 5.0
    url: Optional[List[str]] = None
    zorder: Optional[float] = 1.0
