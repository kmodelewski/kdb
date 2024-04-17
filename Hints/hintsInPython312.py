from typing import override

class Computer:
    def __init__(self, name: str)->None:
        self.name = name

    def turn_on(self)->None:
        print(f'turning on: {self.name} ')

    def turn_off(self) -> None:
        print(f'turning off: {self.name} ')

class Windows(Computer):
    def __init__(self, name:str)->None:
        super().__init__(name)

    @override
    def turn_on(self) ->None:
        print(f'Turning my windows computer')

windows: Windows = Windows('Windows')
windows.turn_on()


#################UNPACK w Python 3.12 ######################
from typing import TypedDict, Unpack

class Item(TypedDict):
    name: str
    value: float

def info(**kwargs: Unpack[Item])->None:
    print(kwargs)

info(name='Pencil',value=10)