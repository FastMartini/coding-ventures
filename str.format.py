
animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item) <------ Using the str.format, we can have more control over this.

print("The {} jumped over the {}".format("cow","moon"))
# or
print("The {} jumped over the {}".format(animal, item))
# or utilizing positional argument
print("The {1} jumped over the {0}".format(animal, item))
# or utilizing keyword argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
# or
text = "The {} jumped over the {}"
print(text.format(animal, item))
#-----------------------------------------------------------------------------------------------------------------------
name = "Diego"

print("Hello, my name is {}.".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))
#-----------------------------------------------------------------------------------------------------------------------
number = 3.14159
number2 = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2))
print("The number is {:o}".format(number2))
print("The number is {:x}".format(number2))
print("The number is {:e}".format(number2))




