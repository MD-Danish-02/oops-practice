class Car:
    total_cars = 0   # class variable

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1   # count increase

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):   # polymorphism
        return "Electric Battery"


# Objects
my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
my_car2 = Car("Honda", "City")

# Outputs
print(my_car.full_name())
print("Fuel:", my_car.fuel_type())

print(my_tesla.full_name())
print("Fuel:", my_tesla.fuel_type())
print("Battery:", my_tesla.battery_size)

print("Total cars created:", Car.total_cars)