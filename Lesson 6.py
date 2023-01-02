from random import randint

my_list = [randint(0,999) for i in range(35)]
print(my_list)
print()

# Task number 1

for value in my_list:
    if value > 100:
        print(value)


# Task number 2

my_results = []
for val in my_list:
    if val > 100:
        my_results.append(val)
print(my_results)


# Task number 3

ind = len(my_list)
sum = my_list[(ind - 1)] + my_list[(ind - 2)]
if ind < 2:
    my_list.append(0)
else:
    my_list.append(sum)
print(my_list)
