# Dictionaries: 1) Dictionaries are ordered collection of data items.
#               2) They store multiple items in a single variable.
#               3) Dictionaries items stored in Key-Value pairs.
#               4) They are separated by commas and enclosed within curly brackets {}.

dic = {
    "INDIA":"Country",
    "Maharashtra":"State",
    "Ritesh":"Human_being",
    123:"Raj",
    234:"Akshay"
}

print(dic["INDIA"])
print(dic["Ritesh"])
print(dic[123])
print(dic)
print(dic.get('Ritesh2'))    #  This key item is not present in dic but it's not showing me Error ,It's showing me None.

# 1) print dict Key pairs 
print(dic.keys())

# 2) print dict values pairs 
print(dic.values())

# 3) Iterate keys one-by-one print values: (Keys Corresponding the value)

for key in dic.keys():
    print(f"The Value corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key, value in dic.items():
    print(f"The Value corresponding to the key {key} is {value}")