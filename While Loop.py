# while loop = a statement that will execute its block of code as long as it's condition remains true.

username = ""
while len(username) == 0:
    username = input("What is your username? ")

print("Hello "+username)

# or

#name = None
#while not name:
    #name = input("Enter your name:")
    #print("Hello "+name)

password = ""
while len(password) == 0:
    password = input("What is your password? ")

print("Welcome "+username+", your password is "+password+".")


