class Car:
    def __init__(self, brand, model):
        self.__brand = brand      # private variable
        self.model = model

    def get_brand(self):          # getter method
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# Car object
my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())        # access via getter
print(my_car.full_name())

# ElectricCar object
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())      # inherited getter
print(my_tesla.full_name())
print(my_tesla.battery_size)