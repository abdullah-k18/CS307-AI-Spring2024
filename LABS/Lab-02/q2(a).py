list1 = [1, 2, [3, 4, 5], 6]
list2 = [7, 8, 9, 10]
print(list1) #nested list
print("Length: ", len(list1)) #length of list
print(list1 + list2) #list concatenation
if 2 in list1: #membership
    print("2 is present in list1")
else:
    print("2 is not present in list1")
for i in list2: #iteration
    print("Iteration:", i)
print("Printing Index:", list1[2]) #indexing
print("Slicing:", list2[1:3])