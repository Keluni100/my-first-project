
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())

