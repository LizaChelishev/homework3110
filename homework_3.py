list1 = [1,2]
list2 = [4,5]
print([list(zip(list1, list2)) + list(zip(list2, list1))])