# Inheritance:- 1) It is an core concepts in Object-oriented programming(OOP) language. 
#               2) It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a
#                  class from another class. 
#               3) Inheritance is the capabilit of one class to derive or inherit the properties from another class. 
#               4) The child class will inherit all the public and protected properties and methods from the parent class.
#               5) It can have its own properties and methods.  

# Types of Inheritance:-
# 1) Single Inheritance
# 2) Multiple Inheritance
# 3) Multilevel Inheritance
# 4) Hierarchi Inheritance
# 5) Hybrid Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name of the Employee is: {self.name} & his/her ID is: {self.id}")

# This is inheritance part:

class programmer(Employee):    # here i have create the programmer class with the help of Employee class(Child class inherits parent class)
    def showLanguage(self):
        print("The default language is python")

obj1 = Employee("Ritesh Gade", 90)
obj1.showDetails()

# obj2 = Employee("Raj", 99)   # This is the normal 
obj2 = programmer("Raj", 90)   # This is an inheritance to derive
obj2.showDetails()

obj2.showLanguage()