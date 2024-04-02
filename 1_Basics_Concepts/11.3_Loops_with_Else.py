# Else statements use in loop: Else block appears after the body of the loop

for i in range(11):
    print(i)

else:
    print("Sorry Loops are Done")

# I ma breaking the loop else statements is not Exicuted: Beacuase the l

for i in range(11):
    print(i)
    if i == 6:
        break
    
else:
    print("This is not Exicuted")
