# Constructor:- 1) Constructor is a special method in a class used to create and initalize an object of a class. 
#               2) A constaructor is a unique function that gets called automatically when an object is created of a class. 
#               3) The main purpose of constructor is to initialize or assign values to the data members of that class.  
#               4) It can not return any value other than None. 
# 
#   
# __init__ is one of the reserved function in python. 
# self is madatory in function with in the class. When i craeting the object it will be called as a constructor

# Types of Constructor in python:-
# 1) Paramenterized Constructor
# 2) Default Constructor

# 1) Paramenterized Constructor:- 1) When the constaructor accepts arguments along with self, it is known as parameterized constructor. 
#                                 2) These arguments can be used inside the class to assign the value to the data members.
class person:

    def __init__(self, n, r):    # I want to give you to n & r as arguments so you can store in it
        print("Hey I am person")
        self.name = n
        self.role = r

    def info(self):
        print(f"{self.name} is a {self.role}")

a = person("Ritesh", "Software Developer")    # called or invoked the init() method 
b = person("Nikita", "HR")                    # called or invoked the init() method 

a.info()
b.info()


# 2) Default Constructor:- 1) When the constructor doesn't accept any arguments from the object and has only one arguments, self in the constructor 
#                             it is known as Default constroctor. 

class Details:
    def __init__(self):
        print("animal crab belongs to crustances group")

obj = Details()
