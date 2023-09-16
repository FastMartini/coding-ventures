# set = a collection which is unordered, and unindexed. No duplicate values.
# .union = combines two variables.
# .update = puts a set in another set.
# .difference = finds all the differences in a variable.
# .intersection = finds all the similarities in a variable.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))



for x in utensils:
    print(x)