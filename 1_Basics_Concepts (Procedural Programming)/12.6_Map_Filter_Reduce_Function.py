# 1) In python, the Map, Filter and Reduce function are built-in function that allow you to apply a function to asequence of elements & return a new sequence.
# 2) These Functions are knows as higher-order functions, as they take other functions as arguments.  

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# 1)Map Function():- 1) The map function applies a function to each elements in sequence  & returns a new sequence containing the transformed elements. 
#                     syntax:- map(function, iterable)
#                    2) The function argument is a function that is applied to each elements in the iterable argument. 
#                    3) The iterable arguments can be a list, tuple, or any other iterable object. 

# This is normal to write:-
def cube(x):
    return x * x * x

l = [1,2,4,6,4,3]
newl = []
for item in l:
    newl.append(cube(item))
print("Normal :-",newl)

# What is shortcut for this by using map:-

l = [1,2,4,6,4,3]
# newl = list(map(cube, l))               # We can use a function argument
newl = list(map(lambda x: x * x * x,l))   # We can use a lambda Function
print("Map output:-",newl)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# 2) Filter Function:- 1) The filter function filters a sequence of elelment based on a given predicate and 
#                         return a new sequence containing only the elements that meet the predicate. 
#                         syntax:- filter(predicate, iterable)
#                      2) The predicate arguments is a function that return a boolean value and is aaplied to each element in the iterable argument. 
#                      3) The iterable arguments cab be list, tuple or other iterable object. 

l = [1,2,4,6,4,3]
def filter_function(a):
    return a > 2

newnewl = list(filter(filter_function, l))
print("Filter Output:- ",newnewl)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# 3) Reduce Function:- 

from functools import reduce

numbers = [1,2,3,4,5,6]

def mysum(x,y):
    return x + y

sum = reduce(mysum, numbers)

print("Reduce Output:- ",sum)