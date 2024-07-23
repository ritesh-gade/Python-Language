# Format:- We can combine String & Number by using the format() method!

# Eg:.1)
age = 24
name = "Ritesh"
txt = "My name is {}, and I am {} year old."
print(txt.format(name,age))

# Eg:.2) 
qty = 3
itemno = 578
price = 89.9
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(qty,itemno,price))

# Eg:.3) We can use index Number {0}
qty = 3
itemno = 578
price = 89.9
myorder = "I want to pay {2} dollars {0} pieces of item {1}."
print(myorder.format(qty,itemno,price))


# f-string in python:- We can prefix the string letter 'f' the string become the f-string itself. The f-string convenient way to embed python expression inside string literals for formating. 

# Eg.1:-
country = "India"
name ="Ritesh"
txt = f"My name is {name} and I am from {country}"
print(txt)

# Eg.2:-
price = 22.206090
new = f"Price of Chips is:-{price:.2f}"
print(new)

# Eg.3:-
print(f"Multiplication:-{22 * 23}")



