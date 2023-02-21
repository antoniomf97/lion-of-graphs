from pydantic import BaseModel
from typing import List, Optional

from _models.image import ImageModel
from _models.data import FileModel, FunctionModel


class PayloadModel(BaseModel):
    data: Optional[List[FileModel | FunctionModel]]
    image: ImageModel = ImageModel()
