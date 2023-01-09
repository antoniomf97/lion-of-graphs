from pydantic import BaseModel


class Title(BaseModel):
    label: str
    color: str
    fontsize: int


class Options(BaseModel):
    color: str
    title: Title
    xlabel: str
    ylabel: str
