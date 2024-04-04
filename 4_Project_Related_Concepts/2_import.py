# importing:- 1) Importing in python is the process of loading code from a python module into the current script. 
#             2) This allows you to use the function and variable defined in the modules in your current script.(imported addition modules are depend on)
#             3) To importing modules in python, you use import statements following name of the module. 


import pandas
import math

result = math.sqrt(9)
print(result)

# from Keyword:- You can also import specific functions or variables from a modules using the from keyword. 
from math import sqrt, pi

result = sqrt(9) * pi
print(result)

# importing everything:- 1) It is also possible to import all functions and variables from a module using the * wildcard. 
#                        2) This is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from. 

from math import *

result = sqrt(134) * pi
print(result)

# as keyword: We want to short form of any function that time we can use as keyword.
 
from math import pi, sqrt as s

result = s(9) * pi
print(result)

# dir Function:- This is built-in function you can view the names of all the functions and variables defined in a modules. 
# import math
# print(dir(math))
# print(math.nan, type(math.nan))

# import flask
# print(dir(flask))

# we can use our own module show below:-
from ritesh import welcome, boy 
welcome()     # Call the Function
print(boy)    # print the boy variable