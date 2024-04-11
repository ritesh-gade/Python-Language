# Return Statements:- Is Used to return the value of the expression bck to thr calling function.

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    
    # return 10
    return sum / len(numbers)

a = average(12,3,12,34,56)          # calling Function usning by return
print(a)