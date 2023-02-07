from pydantic import BaseModel
from typing import Optional, Literal


class Figure(BaseModel):
    figsize: tuple[float] = None
    dpi: float = None
    facecolor = None
    edgecolor = None
    linewidth: float = 0.0
    frameon: bool = None
    subplotpars = None
    tight_layout: bool = None
    constrained_layout: bool = None
    layout: Optional[Literal['constrained', 'tight']]
    kwargs = None
