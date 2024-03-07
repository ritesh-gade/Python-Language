# There are four types of arguments:
# 1) Default Arguments
# 2) Keyword Arguments
# 3) Required Arguments 
# 4) Variable length Arguments

# 1) Default Arguments:- We can provide a default value while creating a function. 
#                        This way the function assumes a default value even if a value is not provided in the function call for that arguments.

def average(a=9,b=2):
    print("The Average of",a,"&",b,"is:",(a+b)/2)

average(4,9)
average()
average(6)
average(b=17)

# 2) Keyword Arguments:- We can change the order of arguments with key=value. Order is not matter.

def average(a=9,b=2):
    print("The Average of",a,"&",b,"is:",(a+b)/2)

average(b=22,a=99)

# 3) Required Arguments:-Necessary to pass the argumets(key=value).

def average(a,b=2):
    print("The Average of",a,"&",b,"is:",(a+b)/2)

average(a=99)  # This is required argumets.


# 4) Variable length Arguments:- Some time we need to pass more arguments than those defined in the actual function.
# there are two ways to achives this:
# # # 1) Arbitrary Arguments:- While creating a function, pass a*before the parameters name while define the function. 
#                            It's processing in the form of tuple.

def average(*numbers):
    print("Type of Arguments Pass:",type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Average of All Numbers is:",sum / len(numbers))

average(12,34,56,74,199)
average(12,45,23)

# # # 2) Keyword Arbitary Arguments:- While creating a function, pass a**before the parameters name while defining the function.
#                                     It's processing in the form of dectionary.   

def name(**name):
    print("Type of Arguments Pass:",type(name))
    print("Hello, My name is :", name["fname"],name["mname"],name["lname"])

last_name = input("Enter Your Surname Name: ")
first_name = input("Enter Your First Name: ")
middle_name = input("Enter Your Middel Name: ")

name(lname = last_name, fname = first_name, mname = middle_name)
    
 