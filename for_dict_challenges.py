# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
def lst_value(lst): # Преобразование списка словарей, в список значений first_name
    lst_val = [x['first_name'] for x in lst]
    return lst_val

stud_list = lst_value(students)
count_students = [print(f'{i}: {stud_list.count(i)}') for i in set(stud_list)]



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
'''
def count_lst(lst): # Преобразование списка в список словарей с количеством значений
    lst_set = [{i: lst.count(i)} for i in set(lst)]
    return lst_set

list_set = count_lst(stud_list) # [{'Петя': 1}, {'Оля': 1}, {'Вася': 1}, {'Маша': 2}]
'''
def max_list(lst):
    return max(set(lst), key=lst.count)

stud_list = lst_value(students) # ['Вася', 'Петя', 'Маша', 'Маша', 'Оля']

print(f'Самое частое имя среди учеников: {max_list(stud_list)}') # Маша




# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
a = [print(f'Самое частое имя в классе {i}: {max_list(lst_value(x))}') 
     for i, x in enumerate(school_students, 1)]


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def lst_value(lst): # Преобразование списка словарей, в список значений first_name
    lst_val = [x['first_name'] for x in lst]
    lst_non = []
    for i in lst_val:
        print(i)
    return lst_non


a = [print(f'Класс {i["class"]}: девочки {len(lst_value(i["students"]))}, мальчики {"fff"}') for i in school]


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

