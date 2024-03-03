# Nested_If:- You can have use if statements inside if statements, this is called nested if statements.

x = int(input("Enter the Number: "))

if (x < 0):
    print("Number is Negative")

elif(x > 0):
    if(x <= 10):
        print("Number is between 1-10")
    elif(x >10 and x<= 20):
        print("Number is between 11-20")
    elif(x >20 and x<= 30):
        print("Number is between 21-30")
    elif(x >30 and x<= 40):
        print("Number is between 31-40")
    elif(x >40 and x<= 50):
        print("Number is between 41-50")
    else:
        print("Number is greater than 50")

else:
    print("Number is Zero")