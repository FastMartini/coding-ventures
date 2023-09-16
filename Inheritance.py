# multi-level inheritance = when a derived (child) class inherits another derived (child) class.
# multiple inheritance = when a child class is derived from more than one parent class.

class Organism:
    alive = True
# -------------------------------------------------

class Animal(Organism):

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")
# -------------------------------------------------

class Prey(Animal):
    def flee(self):
        print("This animal flees.")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting.")
# -------------------------------------------------

class Rabbit(Prey):
    def run(self):
        print("The rabbit is running.")
class Fish(Prey, Predator):
    def swim(self):
        print("The fish is swimming.")
class Hawk(Predator):
    def fly(self):
        print("The hawk is flying.")
# -------------------------------------------------

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.swim()
hawk.fly()
rabbit.run()
# -------------------------------------------------

# method overriding = the ability of an object-oriented programming language to allow a subclass to provide a specific
# implementation of a method that is already provided by its parent.

class Rabbit(Prey):
    def eat(self):
        print("The rabbit is eating a carrot.")

