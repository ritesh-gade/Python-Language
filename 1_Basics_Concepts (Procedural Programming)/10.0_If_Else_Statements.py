# IF_Else:-The Programmer need to check the evaluation(Check the Condition) of certain Expression, It's Evalute True Or False.

# We Can use Conditional(Comparison) Operators to check the condition
# == : Equal
# != : Not Equal
# >  : Greater Than
# <  : Less Than
# >= : Greater than or equal to
# <= : Less than or equal to

# Eg.1) if_else: Check the Condition
a = int(input("Enter Your Age: "))

if (a==18):
    print("Now You Can Register your voting Form")  # Endentetaion(Tab) it's means i am inside the block
    
elif (a<18):
    print("You are not Eligible")

else:
    print("You Are Eligible for Voting")

# Eg.2) elif: We can Exicute number of conditions that time we use elif
num = int(input("Enter the value of num: "))

if (num < 0):
    print("Number is Negative")

elif (num == 0):
    print("Number is Zero")

elif (num == 999):
    print("Number is Special")

else:
    print("Number is Positive")
print("Now I am Happy")