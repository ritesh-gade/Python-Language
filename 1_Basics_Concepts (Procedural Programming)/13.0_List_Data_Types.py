# Lists:- 1) List are ordered collection of data items.
#         2) List are Mutable in python It can modifed after the creation.
#         3) They store multiple items in single variable.
#         4) List items are seprated by commas and enclosed within square brackets[].

list1 = ["Ritesh","Raj","Akshay", 23, 45, True]

subject_marks = [98, 79, 82, 60, 92]

print(subject_marks)
print(type(subject_marks))

# 1) List Index
print(subject_marks[0:]) 
print(subject_marks[1])
print(subject_marks[4])
print(subject_marks[3:-1])
print(subject_marks[-3])
print(list1[1:5])
print(list1[1:5:2])   # list1[start : end : jumpindex]

# 2) check items present or not:-

if "Raj" in list1:
    print("Yes")
else:
    print("No")

# 3) List Comprehension:- Are used for creating new lists from other iterables like lists,tuples,dict,sets,and even in array and string. 

lst = [i for i in range(10)]
print(lst)

lst1 = [i*i for i in range(10)]
print(lst1)

lst1 = [i*i for i in range(10) if i%2==0]
print(lst1)
