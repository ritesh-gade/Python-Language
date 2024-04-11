# Operators: Is used to perform operations on variable and values.
a=25
b=3

# 1) Aithmetic operators:

print(a+b)  #  Addition:
print(a-b)  #  Subtraction:
print(a*b)  #  Multiplication
print(a/b)  #  Division
print(a%b)  #  Modulus
print(a//b) #  Floor Division
print(a**b) #  Exponentiation





# 'is' Vs '==' Operators:- 

a = [11, 43, 99]
b = [11, 43, 99]

print("List :- ",a is b) # Compare the exact location of object in memory. 
print("List :- ",a == b) # Compare the Value

# When we make constant in python like this, then it is made only once in the (Pointing to the same location)memory location(Not going to change & immutable)
a = 9
b = 9

print("Pointing to the same location:- ",a is b)
print("Pointing to the same location:- ",a == b) 

# Tuples are also immutable
a = (2,5)
a = (2,5)
print("Tuple :- ",a is b)
print("Tuple :- ",a == b) 