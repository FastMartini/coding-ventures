# list = used to store multiple items in a single variable.
# .append: to add an item to a pre-existing list.
# .remove: removes an item in a pre-existing list.
# .pop: Will remove the last item in a list.
# .sort: will sort a list in alphabetical order
# .clear: will clear a list




food = ["pizza","hamburger","hotdog","spaghetti"]

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"steak")
food.sort()


for i in food:
    print(i)

# 2D lists = a list of lists

bedroom = ["bed", "night light", "wardrobe"]
kitchen = ["stove", "fridge", "dishwasher"]
living_room = ["T.V.", "couch", "coffee table"]

furniture = [bedroom, kitchen, living_room]

for i in furniture:
    print(i)