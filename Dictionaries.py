# dictionary = a changeable, unordered collection of unique key:value pairs.
#              It is fast because they use hashing, allowing us to access a value quickly
# .get = finds a string within a dictionary.
# .keys = only finds keys within a dictionary.
# .values = only finds values within a dictionary.
# .items = will print the entire dictionary.



capitals = {'USA':'Washington Dc',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)
