# Enumerate Function: 1) It is an built-in function in python.
#                     2) That allow to loop over a sequence(List,Tuple or String). 
#                     3) Get the index & value of each element in the sequence at the same time. 
#                     4) You can use the 'for loop' to unpack tuples and assign them to variable. 

marks = [12,34,56,88,34,9,23,45]

# # This is an Complicated way: 

# index = 0
# for mark in marks:
#     print(index,":-", mark)
#     if(index == 3):
#         print("Ritesh, very Good!!!")
#     index +=1

# # so, If you want to do this in easy way. 

for index, mark in enumerate(marks):
    print(index,":-", mark)
    if(index == 3):
        print("Ritesh, very Good!!!")
        
        
# for index, mark in enumerate(marks, start=1):
#     print(index,":-", mark)
#     if(index == 3):
#         print("Ritesh, very Good!!!")


# # One more Example start at index 1:
# fruits = ["Banana","Apple","Mango","PineApple","WaterMelon"]

# for index, fruit in enumerate(fruits):
#     print(f"{index+1}:-{fruit}")
#     if (index == 2):
#         print("This is my favorite Fruit")