# Car Object
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print(f"{self.brand} {self.model} from: {self.year}")


car1 = Car(brand="Toyota", model="Corolla", year=2016)

car1.show_details()