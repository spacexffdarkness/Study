# Task 1

dict_list = [{'name': 'Danny',
              'age': 15},

             {'name': 'Thomas',
              'age': 42},

             {'name': 'Jade',
              'age': 23},

             {'name': 'Ariadna',
              'age': 33},

             {'name': 'Anthony',
              'age': 56},

             {'name': 'Nataly',
              'age': 79},

             {'name': 'Corey',
              'age': 7},

             {'name': 'Anastasia',
              'age': 7},

             {'name': 'Anna',
              'age': 14},

             {'name': 'Whitney',
              'age': 90},

             {'name': 'Jack',
              'age': 22}]

# item 'a'
"""Создать список и поместить туда имя самого молодого человека.
        Если возраст совпадает - поместить все имена самых молодых."""

youngest = []
y_old = []
for young in dict_list:
    y_old.append(young['age'])
y_old.sort()
for young in dict_list:
    if young['age'] == y_old[0]:
        youngest.append(young['name'])
print(youngest)
# item 'b'
""" Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена."""

longest_name = []
l_name = []
for name in dict_list:
    l_name.append(len(name['name']))
l_name.sort()
for name in dict_list:
    if len(name['name']) == l_name[len(l_name) - 1]:
        longest_name.append(name['name'])
print(longest_name)


# item 'c'
"""Посчитать среднее количество лет всех людей из начального списка."""
num = 0
sum_ages = 0
for mid_age in dict_list:
    sum_ages += mid_age['age']
    num += 1
print(sum_ages/num)


# Task 2
my_dict_1 = {1: 3,
             2: 4,
             5: 4,
             23: 45,
             37: 1}
my_dict_2 = {3: 55,
             76: 22,
             5: 34,
             23: 7,
             44: 87,
             10: 99}

# item 'a'
'''Создать список из ключей, которые есть в обоих словарях'''
list_keys_1 =[]
list_keys_2 = []

result_lists = []
for key_1 in my_dict_1:
    list_keys_1.append(key_1)

for key_2 in my_dict_2:
    list_keys_2.append(key_2)

for i in list_keys_1:
    if i in list_keys_2:
        result_lists.append(i)
print(result_lists)


# item 'b'
'''Создать список из ключей, которые есть в первом, но нет во втором словаре.'''
result_list_1 = []
for var in list_keys_1:
    if var in list_keys_2:
        pass
    else:
        result_list_1.append(var)
print(result_list_1)

# item 'c'
''' Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.'''
result_dict = dict()
for j in my_dict_1:
    if j in result_list_1:
        result_dict[j] = my_dict_1[j]
print(result_dict)


# item 'd'
''' Объединить эти два словаря в новый словарь по правилу:
        если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
        если ключ есть в двух словарях -
        поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}'''
common_dict = dict()
for item in my_dict_1:
    if item in result_lists:
        common_dict[item] = my_dict_1[item], my_dict_2[item]
    else:
        common_dict[item] = my_dict_1[item]
for item_cont in my_dict_2:
    if item_cont in result_lists:
        pass
    else:
        common_dict[item_cont] = my_dict_2[item_cont]
print(common_dict)