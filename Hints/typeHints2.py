# Dictionary hints
from typing import TypedDict, NotRequired, Required


class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: NotRequired[str]


coordinates: Coordinate = {'x': 20, 'y': 20, 'label': 'Warsaw'}

Vote = TypedDict('Vote', {'for': str,
                          'against': str,
                          'topic': Required[str]})

############# LITERALS  ##################

from typing import Literal, TypeAlias

Mode: TypeAlias = Literal['r', 'a', 'w']


def read_file(file: str, mode: Mode):
    print(f'file: {file} in {mode} mode')


read_file("file.txt", 'z')

######### NEW TYPE ########################
from typing import NewType

UserId = NewType('UserId', int)


def get_user(userid: UserId) -> str | None:
    users: dict = {0: 'Mario', 1: 'Krzys'}
    return users.get(UserId(0))


########## SELF ###################
from typing import Self


class File:
    def __init__(self, filepath: str)->None:
        self.filepath = filepath

    @classmethod
    def create_file(cls, name: str, ext: str)->Self:
        return cls(f'{name}.{ext}')

file: File = File.create_file('cat','jpg')
print(file.filepath)


