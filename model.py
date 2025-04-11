# from enum import Enum
#
# class AutoModel(str, Enum):
#     Malibu = "Malibu"
#     BMW = "BMW M5"




# from pydantic import BaseModel
# from typing import Optional
#
# class School(BaseModel):
#     id: int
#     name: str
#     address: Optional[str] = None
#
# class Student(BaseModel):
#     id: int
#     name: str
#     school_id: int
#     grade: Optional[int] = None


from pydantic import BaseModel
from typing import List


class School(BaseModel):
    title: str
    room: List[int]
    teacher: List[str]


class Student(BaseModel):
    name: str
    email: str
    room_id: int
    since: List[str]