# scope = The region that a variable is recognized.
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.
# LEGB Rule = L = Local
#             E = Enclosing
#             G = Global
#             B = Built-in

name = "Diego"  # global scope (available inside & outside functions)

def display_name():
    name = "Martinez"   # local scope (available only inside this function)
    print(name)

print(name)
display_name()