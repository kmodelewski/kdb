#Dictionary hints
from typing import TypedDict, Required
class Coordinate(TypedDict):
    x: float
    y: float
    label: str


coordinates: Coordinate = {'x':20, 'y':20, 'label':'Warsaw'}

Vote = TypedDict('Vote',{'for': str,
                                'against':str,
                                'topic': Required[str]})