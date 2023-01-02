# Task number 3

from random import randint

my_list_1 = [randint(0,100) for i in range(10)]
my_list_2 = [randint(0,100) for j in range(10)]
my_result = []
print(my_list_1)
print(my_list_2)
ind1 = 0
ind2 = 1
for val in my_list_1:
    my_result.insert(ind1, val)
    ind1 += 2
for v in my_list_2:
    my_result.insert(ind2, v)
    ind2 += 2

print(my_result)

# Task number 11

my_str = 'gfgfcjghfcfchbv'
list_of_str = list(my_str)
new_list = []
print(list_of_str)
for i in list_of_str:
    if list_of_str.count(i) == 1:
        new_list.append(i)
print(new_list)
