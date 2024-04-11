# Error Handling: Sometimes when we write the code, we get error in that. whenever a programmer makes a mistake and sometime the mistake can be made by server. 
#                 we don't want our program to stop because of some error, that's why we do error handling in our python program.
#  we using---> Try Except.
# At the time of chances of error in program(halt) that time we used Exception Handling

# Exception Handling: 1) Is the process of responding to unwanted or unexpected events when a computer program runs. 
#                     2) Exception handling deals with these events to avoid the program or system crashing. 
#                     3) Exception would disrupt the normal operation of a program.  

a = input("Enter the Number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
    # print(e)
except:
    print("Invalid Input")
print("Some lines of code ")
print("End of Program")

# We can handle specific errors

try:
    num = int(input("Enter the integer:"))
    a = [12,23,34]
    print(a[num])
    if num < 12:
            print("Hello")

except ValueError:
    print("Number entered is not an interger.")

except IndexError:
    print("Index Error")

except IndentationError:
    print("Indentation error")
