class Car:

    wheels = 4      # class variable

    def __init__(self,make, model, year, color):
       self.make = make     # instance variable
       self.model = model   # instance variable
       self.year = year     # instance variable
       self.color = color   # instance variable

# --------------------------------------------------

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.wheels = 4

print(Car.wheels)