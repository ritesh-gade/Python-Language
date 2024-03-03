# Data types: This is requried in programming to do various operation without causing an error.

# 1) Numeric Data Type:
# a) int:
a=12   
print("The type of a is:",type(a))

# b) float:
b="12.23"
print("The type of b is:",type(b))

# c) Complex:
c = complex(2,8)  # real and Imaginary 
print("The type of c is:",type(c))

# 2) Text Data Type:
# a) String:
d="Hello"
print("The type of d is:",type(d))


# 3) Boolen Type:
d=True
D=False
print("The type of d is:",type(d))
print("The type of D is:",type(D))

# 4) Sequenced Data: Ordered Collection of Data (List & Tuples)
# a) List: are Mutable & can be modified after creation. Enclose within Square brackets[]
list1=[10,12,2,4,-4,["Banana,Apple"],[-3,34]]
print(list1)
print("The type of list1 is:",type(list1))

# b) Tuple: are Immutable & can not be modified after creation. Enclose within round bracket()
tuple1=(("Dog","Cat"),("Mango","Apple"),("Tiger","Lion"))
print(tuple1)
print("The type of tuple1 is:",type(tuple1))

# 5) Maped Data type: Unordered Collection of Data (Dict)
# a) dict: Key:value pair. Enclose in Curly brackets{}
dict1={"Name":"Ritesh","Age":"24","Company":"HCL-Tech"}
print(dict1)
print("The type of dict1 is:",type(dict1))
