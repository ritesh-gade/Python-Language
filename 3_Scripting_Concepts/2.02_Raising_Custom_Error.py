# Raising Custom Error: Sometimes we may need to create our own custom exception that serve our purpose that time we can use raise keyword.

#  What's the reason to create our own custom error(Why should i raise the Error) ?
# ===>  Main reason is stop the program first & nothing unexpected happens. 

# Eg.1)
# a = int(input("Enter any value in between 5 & 9: "))
# if(a<5 or a>9):
#     raise ValueError("value should be between 5 & 9")

# Eg.2)
salary = int(input("Enter salary amout: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")