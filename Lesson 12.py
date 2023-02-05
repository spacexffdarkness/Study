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


def statist_in_json(text_file, list_cen: list):
    """Создает файл stat.json(формат данных JSON) со статисткой(обновляемый) в виде:
       название файла, список слов, сколько раз каждое слово встретилось в тесте"""
    import json
    import re
    with open(text_file) as my_file:
        words = re.findall(r"([a-zA-z\-]+)", my_file.read())
        my_file.close()

    it_is_dict = dict()
    for i in list_cen:
        it_is_dict[i] = words.count(i)

    stat = {str(my_file.name): it_is_dict}
    with open('stat.json', 'w') as json_file:
        json_file.write(json.dumps(stat))

def statist_in_csv(text_file, list_cen: list):
    """Создаёт файл stat.csv(формат данных csv) со статисткой(обновляемый) в виде:
       название файла, список слов, сколько раз каждое слово встретилось в тесте."""
    import csv
    import re
    with open(text_file) as my_file:
        words = re.findall(r"([a-zA-z\-]+)", my_file.read())
        my_file.close()
    data = [[my_file.name]]

    for i in list_cen:
        data.append([i, words.count(i)])

    with open('stat.csv', 'w') as stat_file:
        writer = csv.writer(stat_file)
        for row in data:
            writer.writerow(row)

