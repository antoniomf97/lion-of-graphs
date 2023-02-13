from pydantic import BaseModel, ValidationError, root_validator
from typing import List, Optional

from image import Image


class Data(BaseModel):
    pass


class Function(BaseModel):
    pass


class Payload(BaseModel):
    data_list: Optional[List[Data]] = None
    function_list: Optional[List[Function]] = None
    image_options: Image

    @root_validator
    def check_a_or_b(cls, values):
        if values.get('data_list') is None and values.get('function_list') is None:
            raise ValidationError('')
        return values


if __name__ == "__main__":
    payload_1 = {"data_list": [{"data": "data"}], "image_options": {"image": "image"}}
    payload_2 = {"function_list": [{"function": "function"}], "image_options": {"image": "image"}}
    payload_3 = {"image_options": {"image": "image"}}
    payload_4 = {"data_list": [{"data": "data"}]}

    p1 = Payload(**payload_1)
    print(p1)
    p2 = Payload(**payload_2)
    print(p2)
