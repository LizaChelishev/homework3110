list1 = [1,2]
list2 = [4,5]
print([number for number in zip(*[iter(list1)])])