fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#----------------------------------------------------------------
listData = [5, 10, 25]
x = min(listData)
y = max(listData)
print(x)
print(y)


for i in range(100):
    print(i) 
    #0-99
#----------------------------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1
#----------------------------------------------------------------
for item in range(1,10,3):# start =1, loop= 10 loop, increase 3
    print(item)

#------------------------------
#!Write a Python program to clone or copy a list.

listData = ["kku","ese",64]

def copyList(listData):
    return listData

NewListData = copyList(listData)
print(listData)
print(NewListData)

#*------------------
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


#! Write a Python program to get the difference between the two lists.
list1 = [1, 3, 5, 7, 9,10]
list2=[1, 2, 4, 6, 7, 8]
print(list1)
print(set(list1))
diff_list1_list2 = list(set(list1) - set(list2))
print(diff_list1_list2)
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
