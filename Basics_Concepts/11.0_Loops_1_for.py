# Loops:- Sometimes a programmer wants to execute a group of statements a certain number of times. This case done using loops 
# Classified into Following two types:-
# 1) for loop
# 2) while loop


# 1) for loop:- for loops can iterate over a sequence of iterable objects in python(that is either a list,tuple,dictonary,set & string).
# Eg:-1) String
name =  "Ritesh Gade"

for i in name:
    print(i)
    if(i==" "):
        print("This is Something for special !")

# Eg:-2) List
colors = ["Red","Yellow","Green","Blue","Black"]

for color in colors:
    print(color)
    for i in color:
        print(i)

# We can use range function:

for k in range(5):
    print(k+1)

print("\n")

for k in range(1, 51):
    print(k)

print("\n")

for k in range(1, 20, 2):               # Using steps here gap between start and stop
    print(k)



