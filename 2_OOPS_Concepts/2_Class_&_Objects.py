# Python Class and Objects:

# Class:- 1) A class is a "Blueprint" or a "Template" for creating objects. 
#         2) It's providing initial values for state(Member variable or attributes), & implementations of behavior (Member functions or method). 
#         3) The user-defined objects are created using the class keyword. 

class info:
    name = "Ritesh"
    company = "HCL Tech"
    role = "Software Devloper"
    salary = 20
    def note(self):           # Self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class.  
        print(f"{self.name} is a {self.role}")


a = info()
print(a.name,a.company) 
a.note()      # Call the function which is inside in class info

# Modified the info
b = info()
b.name =input("Enter Your Name: ")
b.role =input("Enter Your Role: ")
print(b.name,b.company) 
b.note()

# Object:- 1) Object is the instance of the class used to access the properties of the class. 

class Details:
    name = "Ritesh"
    age = 25

# we can create no. of objects
obj1 = Details()

obj2 = Details()
obj2.name = "Krunal"

obj3 = Details()
obj3.age = 34

print(obj1.name)
print(obj1.age)

print(obj2.name)
print(obj3.age)

