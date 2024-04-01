# List Methods:- 

# 1) Append - method is used for add data in list at the end. 
list1 = [12,34,56,34,12]
print(list1)
list1.append(99)
print("Add data in end:- ",list1)

# 2) Sort - method is used to update the list in Ascending order.
list2 = [12,3,4,1,13,98]
list2.sort()
print("Update data in Ascending order:-",list2)

# 3) Reverse - reverse the order of the list.  
list3 = [17, 13, 87, 99, 105, 12, 1]
list3.reverse()
print("Reverse the list order: ", list3)

# 4) Index - Give the index place . 
list4 = [12, 34, 45, 56, 13]
b = list4.index(56)
print("Index Place-",b)

# 5) Count - Count the repeted value. 
list5 = [12, 34, 12, 12, 45, 67, 89] 
b = list5.count(12) 
print("Reapeted Count is: ",b)

# 6) Copy - We can copy the list and update. 
list5 = [12, 34, 12, 12, 45, 67, 89]
m = list5.copy()
m[1] = 90
print("Updated List:-",m)

# 7) Insert - We can easy update(Insert) new data in old list. 
list5 = [12, 34, 12, 12, 45, 67,"hello",25]
list5.insert(7,"Ritesh")
list5.insert(1,12)
print("Updated List:-",list5)

# 8) Extend - We can add one list into other list. 
list1 = ["Ritesh","Akshay","Raj","Krushna","Rupesh"]
list2 = ["Radhika","Rutuja","Poonam","Snehal"]
list1.extend(list2)
print(list1)

Bhatakanti = list1 + list2
print("Bhatakanti Group:-",Bhatakanti)
