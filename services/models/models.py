from pydantic import BaseModel


class Options(BaseModel):
    title: str
    xlabel: str
    ylabel: str
