x = int(input("Which Table You want to Generate: "))

for i in range(12):
    if(i == 10):                     #   I used break statement for learning purpose
        break
    print(x, "X", i+1,"=",x * (i+1))
    