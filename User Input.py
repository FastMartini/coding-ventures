name = ""
age = int
player = None
choices = ["yes", "no"]

while len(name) == 0:
    name = input("Hello there, what is your name weary traveller? ")
while age == int:
    try:
        age = int(input("ah, so our warrior's name is " + name + "... how old are you then? "))
        print("oh, so you are " + str(age) + " years old... well then, it is nice to meet you " + name + "!")

    except ValueError:
        print("That is not a number silly")



while player not in choices:
    player = input("Are you ready to embark on your next challenge? ").lower()

if player == "yes":
    print("Ah, there is hope after all! Till we meet again " + name + "!")

else:
     print("It is alright, even the bravest of warriors need to collect their thoughts. Talk to me when you are ready.")













