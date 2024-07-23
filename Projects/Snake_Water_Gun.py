import random

comp = random.randstr("snake", "water" ,"gun")
user = input("Enter your choice (snake, water & gun):-")

def check(comp, user):
    if comp == user:
        print("It's a draw (You have choose the same option)")

    elif (comp == 0 and user == "water"):
        print("You are looser(Computer selected snake)")

    elif (comp == 1 and user == "gun"):
        print("You are looser(Computer selected water)")

    elif (comp == 2 and user == "snake"):
        print("You are looser(Computer selected gun)")

    else:
        print("You are winner !!!!!!!")

check(comp, user)