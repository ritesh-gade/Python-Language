# Dictionaries Methods:
# 1) Update(): We can easily add items
 
frd = {
    "m1":"Raj",
    "m2":"Rupesh",
    "m3":"Akshay",
    "m4":"Krushna"
}

frd.update({"f1":"Radhika"})
print(frd)

frd1 = {
    "f2":"Poonam",
    "f3":'Neelam',
    "f4":"Rutuja",
    "f5":"Snehal"
}

frd.update(frd1)
print(frd)

# 2) clear():Clear the all items in dict (Print the Empty Dict)

frd1.clear()
print(frd1)

# 3) pop(): remove the key-value pair
frd2 = {
    "f2":"Poonam",
    "f3":'Neelam',
    "f4":"Rutuja",
    "f5":"Snehal"
}

frd2.pop("f5")
print(frd2)

# 4) popitem(): Remove the last iteam in dict
frd3 = {
    "f2":"Poonam",
    "f3":'Neelam',
    "f4":"Rutuja",
    "f5":"Snehal"
}

frd3.popitem()
print(frd3)

# 5) del: We can delete the dict
frd3 = {
    "f2":"Poonam",
    "f3":'Neelam',
    "f4":"Rutuja",
    "f5":"Snehal"
}
# del frd3
del frd3["f5"]
print(frd3)

