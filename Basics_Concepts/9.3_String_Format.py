# Format:- We can combine String & Number by using the format() method!

# Eg:.1)
age = 24
txt = "My name is Ritesh, and I am {} year old."
print(txt.format(age))

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