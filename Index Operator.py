# index operator [] = gives access to a sequence's element (str, list, tuples).
# .islower = checks if a certain letter is lower cased.
# .isupper = checks if a certain letter is capitalized.

name = "diego martinez!"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[:5].upper()
last_name = name[6:14].upper()
last_character = name[-1]

print(first_name, last_name, last_character)