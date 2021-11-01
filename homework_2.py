some_list = [1,4,7,12,19,22, 23, 26]
print([str(number) + ' is even' for number in some_list if number % 2 == 0 and str(number) + 'is odd' if number % 2 != 0])