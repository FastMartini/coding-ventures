# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?"))

if age == 100:
    print("WOW!You are a century old!")
elif 18 <= age <= 29:
    print("You are an adult, congratulations!")
elif age <= 0:
    print("How are you even typing this??")

elif 30 <= age <= 99:
    print("you've grown to be such a wise human!")
elif age >= 101:
    print("You are very healthy!")

elif age == 17:
    print("You are in the home stretch pal! Just one more year and you can call yourself a young adult!")
else:
    print("You've still got a lot of growing to do!")