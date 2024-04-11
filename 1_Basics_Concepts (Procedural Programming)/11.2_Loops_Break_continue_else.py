# 1) Break in loop:- We can stop the loop even while loop condition is true(Skip over a part of the code).

i = 1
while i < 10:
  print(i)
  if i == 7:
    print("Break the Statement")
    break
  i += 1

# 2) Continue in loop:- Skip the iteration which you can define and continue to the next. 

i = 0
while i < 12:
  i += 1
  if i == 9:
    print("Skip the iteration:", i)
    continue
  print(i)

# 3) Else statements use in loop

count = 5
while (count > 0):
    print(count)
    count = count - 1

else:
    print("I am Inside Else")

# 4) Do while loop:
i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break