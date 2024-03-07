# Function:- A function is a block of code that performs a specific task whenever it is called. 

# There are two types of Functions:
# 1) Built-in function
# 2) User_defined Function

# 1) Built-in function:- These function are defined and pre-coded in python, some examples of built-in function are as follows:
#                       main(),max(),len(),sum(),type(),range(),print(),dict(),list(),tuple(),set(),etc.

# 2) User_defined Function:- We can create function to perform specific tasks as per our needs.

# Eg:- 1) Calculate Gemotric mean:-

def calculateGmean(a,b):                    # Create a function, we can use this function various times
    mean = (a*b)/(a+b)
    print("Gemotric Mean of ",a ,"and ",b,": ",mean)


# a = int(input("Enter the value of A: "))
# b = int(input("Enter the value of B: "))
# c = int(input("Enter the value of C: "))
# d = int(input("Enter the value of D: "))

# gmean = (a*b)/(a+b)
# print(gmean)

# gmean = (c*d)/(c+d)
# print(gmean)

# calculateGmean(a,b)     # Called the function
# calculateGmean(c,d)     # Called the function

# Eg:- 2) Find the greater number 

def greater(a,b):
    if(a == b):
        print(a,"is equal to",b)
    elif(a > b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

greater(a,b)

c = int(input("Enter the value of C: "))
d = int(input("Enter the value of D: "))

greater(c,d)
    