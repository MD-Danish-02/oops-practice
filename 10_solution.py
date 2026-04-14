class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_info():
        return "Cars are vehicles used for transportation."


class Battery:
    def battery_info(self):
        return "This car uses a lithium-ion battery."


class Engine:
    def engine_info(self):
        return "This car has an advanced electric engine."


class ElectricCar(Car, Battery, Engine):   # multiple inheritance
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
print("Fuel:", my_car.fuel_type())

print(my_tesla.full_name())
print("Fuel:", my_tesla.fuel_type())
print("Battery Size:", my_tesla.battery_size)

# Multiple inheritance methods
print(my_tesla.battery_info())
print(my_tesla.engine_info())

# Static method
print(Car.general_info())

# Class variable
print("Total cars created:", Car.total_cars)

# isinstance checks
print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))
print(isinstance(my_car, ElectricCar))