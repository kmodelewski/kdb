from typing import Any, Final, Iterable, Sequence, Callable, Protocol

# Exercise 1
CONSTANT: Final[int] = 2


# Exercise 2
def get_repr(obj: Any) -> object:
    return repr(obj)


my_repr: Any = get_repr('I love typing!')
print(my_repr)

# Exercise 3
numbers: list[int] = [20, 5, 30, 100]


def get_first_element(elements: Sequence):
    return elements[0] if elements else -1


print(get_first_element(numbers))


# Exercise 4:
def say_hello(person: str, greeting: str):
    print(f'{greeting}, {person}!')


def greet(people: Iterable, greeting: str, hello_func: Callable[[str, str], None]) -> None:
    for person in people:
        hello_func(person, greeting)


friends = ['Mario', 'Luigi', 'James']
greet(friends, 'Yo', say_hello)


# Exercise 5:
class Camera(Protocol):
    def take_picture(self):
        ...

    def turn_on(self):
        ...

    def turn_off(self):
        ...


def automate_photo(camera: Camera)->str:
    camera.turn_on()
    photo = camera.take_picture()
    camera.turn_off()

    return photo


class Canon:
    def __init__(self, name):
        self.name = name

    def take_picture(self):
        print(f'{self.name} took a picture!')
        return 'image.jpg'

    def turn_on(self):
        print(f'Turning on {self.name}.')

    def turn_off(self):
        print(f'Turning off {self.name}...')


my_camera: Camera = Canon('CanonDigital')
automate_photo(my_camera)


class Car:
    name = "Ford"

    def __repr__(self):
        return 'Hello ' + self.name


print(repr(Car()))
