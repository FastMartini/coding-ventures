# tuple = collection which is ordered and unchangeable. It is used to group together related data.
# .count = counts how many of the same strings there are in a variable.
# .index = finds the position of a string in a variable.

student = ("Diego", 17, "male")

print(student.count("Diego"))
print(student.index("male"))

for x in student:
    print(x)

if "Diego" in student:
    print("Diego is a student!")