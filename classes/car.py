class Car:

    def __init__(self, make, model, year):
        '''Initialize attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        '''Return a neatly fomratted descriptive name.'''
        long_name = f" This is fuel car: {self.year}/{self.model}/{self.make}/{self.odometer_reading}"
        return long_name.title()

    def modify_odometer(self, driven_distance):
        self.odometer_reading += driven_distance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #super calls a method from the parent class

    def get_descriptive_name(self) -> str:
        long_name = f" This is electric car: {self.year}/{self.model}/{self.make}/{self.odometer_reading}"
        return long_name.title()

audi = Car('audi','a4',2023)
print(audi.get_descriptive_name())

audi.modify_odometer(10)
print(audi.get_descriptive_name())

tesla = ElectricCar('tesla','t1',2023)
print(tesla.get_descriptive_name())

