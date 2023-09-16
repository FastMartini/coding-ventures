# logical oerators (and,or,not) = used to check if two or more conditional statements is true
# not = changes statements that are normally true to false and vice versa.

temp = int(input("what is the temperature outside?"))


if temp >= 0 and temp <= 30:
    print("the temperature is rather nice today!")
    print("go outside and get some fresh air!")
elif temp < 0 or temp > 30:
    print("the temperature is doesn't seem to good today!")
    print("You should probably stay inside.")

#the not statements
if not(temp >= 0 and temp <= 30):
    print("the temperature is doesn't seem to good today!")
    print("You should probably stay inside.")
elif not(temp < 0 or temp >30):
    print("the temperature is rather nice today!")
    print("go outside and get some fresh air!")
