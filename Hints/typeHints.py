from datetime import datetime
from typing import Callable


def print_it(text: str, print_func: Callable[[str], None]) -> None:
    print_func(text)


def loud_print(text: str) -> None:
    print(f'{text}!')


print_it("hello", loud_print)


###################

from typing import Protocol

class Printer(Protocol):
    def print(self, magazine:str)->None:
        ...

    def copy(self, magazine:str, copies: int)->None:
        ...


class LaserPrinter:
    def __init__(self, name: str, version:int)->None:
        self.name = name
        self.version = version

    def print(self, magazine: str) -> None:
        print(f'{self.name} ({self.version}) is printing: "{magazine}".')

    def copy(self, magazine: str, copies: int) -> None:
        print(f'{self.name} ({self.version}) is making {copies} copies of : "{magazine}".')


lp: Printer = LaserPrinter('Laser printer', 1)

def print_magazine(printer: Printer, magazine: str)->None:
    printer.print(magazine)
    printer.copy(magazine, 5)

print_magazine(lp, 'Python files')
