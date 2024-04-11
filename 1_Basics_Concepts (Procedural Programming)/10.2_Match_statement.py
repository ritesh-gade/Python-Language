# Match case:- It's like characteristics very similar to if-else Functionality. It will be compare a given variable value to different shapes, also referred to the pattern

x = int(input("Enter the value of X: "))

match x:
    case 0:
        print("x is zero")

    case 1:
        print("This case is 1")

    case 2:
        print("This case is 2")

    case 3:
        print("This case is 3")

    case 4:
        print("This case is 4")
    
    case 5:
        print("This case is 5")
    
    case _ if (x >= 6 and x <= 10):
        print("Your Number is between 6-10")

    case _ if (x >= 11 and x <= 20):
        print("Your Number is between 11-20")

    case _:             # Default case
        print("You Enter: ",x)
