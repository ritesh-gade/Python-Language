# Set: Set is a collection of well defined objects.
#      Sets are unordered  collection of data items. They store multiple items in a single variable. 
#      Set items are seprated by commas & enclosed within curly brackets{}. 
#      Set are unchangeable, means you can't change items of the set once created & it's do not contain duplicate items.


set1 = {12,23,12,35,56,12,34,12}
print(set1)

set2 = {"Ritesh",12,True,12,"123",None}
print(set2)

ritesh = {}
print(type(ritesh))

ritesh1 = set()
print(type(ritesh1))

# Set in Loop:
for value in set2:
    print(value)

