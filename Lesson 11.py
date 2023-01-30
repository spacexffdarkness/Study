def censored(text_file, list_cen: list):
    """На вход функция получает имя файла и список слов для замены,
       функция ничего не возвращает, но в результате ее работы необходимо создать файл,
       в котором слова из списка заменены шаблоном(*)"""
    import re
    with open(text_file) as my_file:            # Получаем список слов из файла
        words = re.findall(r"([a-zA-z\-]+)", my_file.read())
        my_file.close()

    new_list = []               # Получаем список после цензурирования
    for i in words:
        if i in list_cen:
            new_list.append('***')
    else:
        new_list.append(i)

    sym_list = []                #Получаем список символов и пробелов для восстановления текста
    with open(text_file) as my_file:
        for line in my_file:
            for symb in line:
                if not symb.isalpha() is True:
                    sym_list.append(symb)
        my_file.close()

    exclusion_list = [',', '\n', ';', ':', '!', '?', ']', ')', '%', '\"', '$', '&', '-']
    ind = 1
    for j in sym_list:        # Совмещаем списки
        if j.isalnum() is True or j in exclusion_list:
            new_list.insert(ind, j)
            ind += 1
    else:
        new_list.insert(ind, j)
        ind += 2

    new_string = ''.join(new_list)
    new_file = open('censored_file.txt', 'w')    #Создаем файл
    new_file.write(new_string)
