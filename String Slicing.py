# slicing = creates a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]
# start = is inclusive, therefore it starts with 0
# stop = is exclusive, therefore it starts with 1
# step = how much you are increasing an index by between starting and stopping.

name = "Diego Martinez"

first_name = name[0:5]  # [0:5] or [:5]
last_name = name[6:14]  # [6:14] or [6:]
funky_name = name[0:14:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://ritzycleaningservices.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])