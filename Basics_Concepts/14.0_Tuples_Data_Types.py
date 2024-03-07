# Tuples:- 1) Tuples are ordered collection of data items.
#          2) Tuples are Immutable in python It can not modifed after the creation.
#          3) They store multiple items in single variable.
#          4) Tuples items are seprated by commas and enclosed within round brackets().

tup = (13, 16, 15,"Ritesh",23,45,78)
print(type(tup),tup)

# Index Tuples
print(tup[-1])
print(tup[2:])
print(tup[0:3])
print(tup[0:3:2])


# Statements Use in Tuples:
if 16 in tup:
    print("Yes 16 is present in this tuples")
else:
    print("No 16 is not present in this tuple")

# We can create new tuple with the help of old tuple
tup2 = tup[2:5]
print(tup2)