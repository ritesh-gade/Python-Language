# Finally Clause: 1) Finally code is a part of Exception handling. When we handle exception using try and except block, we can include a finally block at the end. 
#                 2) The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message. 

def func1():
    try:
        l = [12,34,45,67,1,2,46]
        a = int(input("Enter the Index Number: "))
        print(l[a])
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("I am always Executed")

    # print("I am always Executed")

x = func1()
print(x)