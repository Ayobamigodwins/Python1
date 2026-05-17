class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting...")

    def stop(self):
        print(f"{self.make} {self.model} has stopped.")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def honk(self):
        print("Beep beep!")


class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type

    def pop_wheelie(self):
        print("Doing a wheelie!")


# Demo
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()

my_bike = Bike("Trek", "FX3", "hybrid")
my_bike.start()
my_bike.pop_wheelie()
my_bike.stop()