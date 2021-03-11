list1 = [1,3,5,7,9,11] #list1 is consist of odd numbers 1 to 11
list2 = [2,4,6,8,10,12] #list2 is consist of even numbers 2 to 12

list3 = list1 + list2 #Merge these two lists
print(list3)

list4 =[i*2 for i in list3] #Multiply all values in the list3 by 2

print(list4)

for i in list4:
    print(f'{i} type is :' ,type(i)) #I use for loop to print the data type of all values in the list4
