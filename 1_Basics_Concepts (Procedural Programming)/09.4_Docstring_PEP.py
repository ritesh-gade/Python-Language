# Docstring :- (Function with Description).  -------> They are used to documnets our codes.
#               Python decstring are the string literals that appear right after the definition of a function, method, class, or module.

def square(a):
    '''Give me a Square of User input Number:-'''    # This is Docstring
    print(a**2)

a = int(input("Enter the number:- "))
print(square.__doc__)                               # How to see the docstring
square(a)



# PEP 8:- (GuideLine and Beast practice provide for python ---> Focus is Consistent, readable, and maintainable)(PEP---> Python Enhancement Proposal)
#           PEP is a document that provide guidlines and beast practices on how to write python code. 


# The Zen of Python:- (Ths is a Poem)----> Easter Egg is inserted in python. 
#                       Long time pythoneer Tim peters succinctly channels the BDFL's guiding principles for python design. 


import this