class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine of the", self.make, self.model, "is starting.")

    def stop_engine(self):
        print("The engine of the", self.make, self.model, "is stopping.")

    def honk_horn(self):
        print("Honk! Honk!")

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Accessing attributes of car1
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car1.year)  # Output: 2022

# Calling methods of car2
car2.start_engine()  # Output: The engine of the Honda Accord is starting.
car2.honk_horn()  # Output: Honk! Honk!
car2.stop_engine()  # Output: The engine of the Honda Accord is stopping.
