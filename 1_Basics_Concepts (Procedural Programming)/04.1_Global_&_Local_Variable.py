# Local & Global variable :

# Local Variable: Local variable is an variable that is defined with in a function and is only accessible within that function.It is created when the function is called. 

# Global Variable: Global variable is a variable that is defined outside of a function and is accessible from within and function in your code. 


l = 12          # This is a global variable it is accesible in any function. 
print(f"Global variable x is: {l}")


def function1():
    x = 23              # This is a local variable
    y = 18              # This is a local variable 
    global l            
    l = 29                 
    print(f"Local variable x is: {x}")
    print(f"Local variable x is: {y}")

function1()

print(f"Global variable x is: {l}")

# print(f"Local variable x is: {y}")     # y is an local variable that's why it won't work outside the function. 

