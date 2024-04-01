# Methods of sets:

# 1) Find the Union & Intersection in 2 Sets:
s1 = {2,3,5,6,8,6}
s2 = {7,8,9,5,1,8,3}
print("(S1 U S2) = ",s1.union(s2))
print("(S1 n S2) = ",s1.intersection(s2))

# 2) Update the old set into new/new set into old:
old = {2,3,5,6,8,6}
new = {7,8,9,5,1,8,3}
new.update(old)
print(new)

# 3) Not common in two or more sets will be printed by using symetric_difference:
state1 = {"MH", "MP", "UP", "GA", "MN", "ML", "AN", "CH"}
state2 = {"GJ", "MN", "OR", "RJ", "KL", "UP", "CH", "DL"}
state3 = state1.symmetric_difference(state2)
print(state3)

# 4) Update the set which data is new:
state1 = {"MH", "MP", "UP", "GA", "MN", "ML", "AN", "CH"}
state2 = {"GJ", "MN", "OR", "RJ", "KL", "UP", "CH", "DL"}
state1.symmetric_difference_update(state2)
print(state1)

# 5) isdisjoint(): This method checks if items of given set are present in another set, This method given True or False.
state1 = {"MH", "MP", "UP", "GA"}
state2 = {"GJ", "MN", "OR", "RJ"}
print(state1.isdisjoint(state2))

# 6) issuperset(): Check the set is superset or not
state1 = {"MH", "MP", "UP", "GA"}
state2 = {"GA", "MH"}
state3 = {"GJ", "MN"}

print(state1.issuperset(state2))
print(state1.issuperset(state3))

# 7) issubsate(): Check the all items are present in particular set
state1 = {"MH", "MP", "UP", "GA"}
state2 = {"GA", "MH"}
state3 = {"MH", "MN"}

print(state2.issubset(state1))
print(state3.issubset(state1))

# 8) difference(): Which value is not present in set:-
state4 = state1.difference(state2)
print(state4)

# 9) add(): add item in particular set
frd = {"krushna","Rupesh","Radhika","Rutuja","Raj"}
frd.add("Akshay")
print(frd)

# 10) remove(): remove the iteam if item is not present showing the Error/ discard(): if item is not present not showing the Error
frd = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
frd.remove("Snehal")
print(frd)
frd2 = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
frd2.discard("Snehal2")
print(frd2)

# 11) pop(): Remove any random item in set
frd1 = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
frd2 = frd1.pop()
print(frd1)
print(frd2)

# 12) del(): delete overall set
frd2 = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
# del frd2      # Showing the NameError
# print(frd2)

# 13) clear(): claer all item in the set
frd2 = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
frd2.clear()
print(frd2)

# if item check with set used in keyword:
frd2 = {"krushna","Rupesh","Radhika","Rutuja","Raj","Akshay","Snehal"}
if ("Rupesh" in frd2):
    print("Rupesh is presnt in frd2")
else:
    print("Rupesh is not Present in frd2")
# Unchangeable
print(s1 ,s2)