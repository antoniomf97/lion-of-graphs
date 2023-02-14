from pydantic import BaseModel
from typing import List, Optional

from image import Image
from data import File, Function


class Payload(BaseModel):
    data: Optional[List[File | Function]] = None
    image: Image = Image()


if __name__ == "__main__":
    payload_1 = {"data": [{"filename": "file"}]}
    payload_2 = {"data": [{"function": "$function$"}]}

    p1 = Payload(**payload_1)
    print(p1) 
    p2 = Payload(**payload_2)
    print(p2)
