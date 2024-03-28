# Recursion Function:- Recursion is basically functions, But when inside a function you call the same function it's called recursion.(Call itself)


# calcultae Recursion factorial:
# factorial(7) = 7*6*5*4*3*2*1
# factorial(n) = n * factorial(n-1)

def factorial(num):
    if (num == 0 or num == 1):
        return 1

    else:
        return (num * factorial(num - 1))
        # print(num * factorial(num - 1))
    

# User Input & call to the function:
num = int(input("Enter the factorial Number: "))
print(factorial(num))