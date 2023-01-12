# Task 1
def changing_str_list(my_list):
    """Функция возвращает новый список в котором содержаться
       элементы из my_list по следующему правилу:
       Если строка стоит на нечетном месте в my_list, то ее заменить на
       перевернутую строку. "qwe" на "ewq".
       Если на четном - оставить без изменения."""
    new_list = []
    index = 0
    for i in my_list:
        if index % 2 == 0:
            rev = i[::-1]
            new_list.append(rev)
        else:
            new_list.append(i)
        index += 1
    return new_list


# Task 2
def find_sym_a_in_strings_of_my_list_if_it_is_first(my_list):
    """Функция возвращает новый список в котором содержаться
       элементы из my_list у которых первый символ - буква 'a'."""
    new_list = []
    for i in my_list:
        if i[0] == 'a':
            new_list.append(i)
    return new_list


# Task 3
def find_sym_a_in_strings_of_my_list(my_list):
    """Функция возвращает новый список в котором содержаться
       элементы из my_list в которых есть символ - буква 'a' на любом месте."""
    new_list = []
    for i in my_list:
        for j in i:
            if j == 'a':
                new_list.append(i)
    return new_list


# Task 4
def find_str_in_my_list(my_list):
    """Функция возвращает новый список в котором содержаться только строки из my_list."""
    new_list = []
    for i in my_list:
        typ = type(i)
        if typ == str:
            new_list.append(i)
    return new_list


# Task 5
def find_sym_that_used_one_time(my_str):
    """Функция возвращает новый список в котором содержаться те символы из my_str,
       которые встречаются в строке только один раз."""
    new_list = []
    my_list = list(my_str)
    for i in my_list:
        if my_list.count(i) > 1:
            pass
        else:
            new_list.append(i)
    return new_list


# Task 6
def if_it_exist_in_a_both_str(str_1, str_2):
    """Функция возвращает список в который поместить те символы,
       которые есть в обеих строках хотя бы раз."""
    set_1 = set(str_1)
    list_1 = list(set_1)
    list_2 = list(str_2)
    new_list = []
    for i in list_1:
        if i in list_2:
            new_list.append(i)
    return new_list


# Task 7
def if_it_exist_only_once_in_both_str(str_1, str_2):
    """Функция возвращает список, в который поместить те символы, которые есть в обеих строках,
       но в каждой только по одному разу."""
    list_1 = list(str_1)
    list_2 = list(str_2)
    new_list_1 = []
    new_list_2 =[]
    new_list = []
    for i in list_1:
        if list_1.count(i) == 1:
            new_list_1.append(i)
    for j in list_2:
        if list_2.count(j) == 1:
            new_list_2.append(j)
    for item in new_list_1:
        if item in new_list_2:
            new_list.append(item)
    return new_list
