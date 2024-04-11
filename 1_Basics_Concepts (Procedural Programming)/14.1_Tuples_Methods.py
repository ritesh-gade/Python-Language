# Tuples Methods:-
# 1) Manipulating Tuples:- Tuples are immutable, Hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list.
#                          Then Perform operation on that list and again convert it back into Tuple. 

countries = ("India","Spain","Italy","England","Autralia","Germany")

temp = list(countries)           # Convert Tuple into list
temp.append("South-Africa")      # Add one country intpo list
temp.reverse()                   # Revese the list
temp.pop(4)
print(temp)
temp[4] = "West-Indies"
print("This is List:-",temp)
countries = tuple(temp)         # Convert List Into Tuple

print("This is Tuple:-",countries)

# 2) Count:- We can Count the Repeted Number 
tuple1 = (1,3,45,5,6,7,4,3,6,4,3,2,6,6)
tuple2 = tuple1.count(6)
print("Count of 6 in tuple is:-",tuple2)

# 3) index:- Give the index count
tuple2 = tuple1.index(2)
print("2 Is an index:-",tuple2)
tuple2 = tuple1.index(3, 4, 10)  # Slicing the tuples and give the index(element, start, end)
print(tuple2)

# 4) len:- Find the length of Tuples
tuple2 = len(tuple1)
print("Length of Tuple is:-",tuple2)



