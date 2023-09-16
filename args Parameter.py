# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

#def add(num1, num2):
    #sum = num1 + num2
    #return sum                  # Will give you an error as add( takes 2 positional arguments but 3 were given

#print(add(1, 2, 3))


def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))


# **kwargs = parameter that will pack all arguments into a dictionary.
#            Useful so that a function can accept a varying amount of keyword arguments.

#def hello(first, last):
    #print("Hello "+first+" "+last)                          # Will give you an error as there is an unexpected keyword argument

#hello(first="Diego",middle="Miguel", last="Martinez")


def hello(**kwargs):
    #print("Hello "+ kwargs['first']+" "+ kwargs['last'])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value)
hello(first="Diego",middle="Miguel", last="Martinez")