class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model   # make model private
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand

    @property
    def model(self):   # read-only property
        return self.__model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_info():
        return "Cars are vehicles used for transportation."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Battery"


# Objects
my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Outputs
print(my_car.full_name())
print("Model:", my_car.model)

print(my_tesla.full_name())
print("Model:", my_tesla.model)
print("Battery:", my_tesla.battery_size)

print(Car.general_info())
print("Total cars created:", Car.total_cars)