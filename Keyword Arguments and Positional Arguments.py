# Keyword Arguments = arguments preceded by an identifier when we pass them to a function.
#                     The order of the arguments does not matter, unlike positional arguments.
#                     Python knows the names of the arguments that our function recieves.

# function = a block of code which is executed only when it is called.


def hello(first_name, last_name, age):
    print("Hello "+first_name+" "+last_name+"!")            # Positional Arguments
    print("You are "+str(age)+" years old.")
    print("Have a nice day!")

hello("Diego", "Martinez", 17)


def Hello(first_name, last_name, age):
    print("Hello "+first_name+" "+last_name+"!")            # Keyword Arguments
    print("You are " + str(age) + " years old.")
    print("Have a nice day!")

Hello(age="17", last_name="Martinez", first_name="Diego")

