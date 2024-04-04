# if __name__ == "__main__":-1) This is an idiom is a common pattern used in python scripts to determine whether the scripts is being run directly
#                               or being import into another scripts.(The Check is placed to not execute it)
#                            2) In python, the "__name__"variable is built-in variable that is automatically set to the name the current modules. 
#                            3) When a python scripts is run directly, the "__name__" variable is set to the string "__main__". 
#                            4) When the scripts is imported as a module into another is scripts, the "__name__" variable is set to the name of the module. 


# I am using this concept from ritesh.py python file. 
# if __name__ == "__main__":-  "__name_":- Where it is being printed from  & "__main__":- main means it is being run from here itself. 
# print(__name__)
# if __name__ == "__main__":
#     welcome()

import ritesh                   # my own module 
ritesh.welcome()