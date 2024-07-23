# Access Specifiers/Modifiers:- It is used to limit the access of class variable and class methods 
#                               outside of the class while implementing the concepts of inheritance. 

# Types of access Specifilers:- 
# 1) Public access modifier 
# 2) Private access modifier 
# 3) Protected access modifier 

# 1) Public access modifier:- 1) All the variable & methods(member functions) in python are by default public. 
#                             2) Any instance(Object) variable in a class followed by the 'self' keyword i.e: self.var_name are public accessed. 

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
obj1 = student("Ritesh", 25)
print(obj1.name)
print(obj1.age)

# 2) Private access modifier:- 1) Private member of class(variable or methods) are those memmber which are only accessible inside the class. 
#                                 we can't use private member outside of class. 
#                              2) We can indicate private by prefixing its name with double underscore(__). 
#                              3) We can be accessed indirectly by using name mangling to single underscore before the class name just like(_ClassName__variable)

# Not access by usning double underscore(__):-
class student:
    def __init__(self, age):
        self.__age = age
    
obj1 = student(25)
# print(obj1.__age)   # Not Acees It's showing Error, you can Check with uncommnet. 

# access indirectly by using Name Mangling
# Name Mangling:- It ia an technique used to protect-class-private & superclass-private attribute from accidentally overwritten by subclasses. 
class student:
    def __init__(self, age):
        self.__age = age
    
obj2 = student(25)
print(obj2._student__age)


# 3) Protected access modifier:- 1) Members(Methods & Attributes) declared as protected are accessible only within the class itself and derived class(SubClass).
#                                2) To declare a data member as protected, use a single uderscore (_) before its name. 

class Student:
    def __init__(self):
        self._name = "Ritesh"

    def _funName(self):         # Protected Method
        return "I am learning OOP Concepts"
     
class Subject(Student):         # Inherited class
    pass

obj1 = Student()
obj2 = Subject()

# Calling by object of Student class
print(obj1._name)
print(obj1._funName())

# Calling by object of Subject class
print(obj2._name)
print(obj2._funName())
