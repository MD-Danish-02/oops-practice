class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"Car: {self.brand}, Speed: {self.speed} km/h")

c1 = Car("BMW", 220)
c1.show()