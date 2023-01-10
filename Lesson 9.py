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
              'age': 32},

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



# item 'c'
"""Посчитать среднее количество лет всех людей из начального списка."""
