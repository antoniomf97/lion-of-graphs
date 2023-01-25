from pydantic import BaseModel
from typing import Optional, List


class Title(BaseModel):
    label: str
    color: str
    fontsize: int


class Plot(BaseModel):
    index: str
    label: str
    showPoints: bool
    showLines: bool
    linesColor: Optional[str]
    pointsColor: Optional[str]


class Figure(BaseModel):
    title: Title
    xlabel: str
    ylabel: str
    grid: bool


class Options(BaseModel):
    figure: Figure
    plots: List[Plot]
