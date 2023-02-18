from pydantic import BaseModel
from typing import List, Optional

from image import ImageModel
from data import FileModel, FunctionModel


class PayloadModel(BaseModel):
    data: Optional[List[FileModel | FunctionModel]] = None
    image: ImageModel = ImageModel()
