from mypy.binder import Union


def find_same_numbers(list1: Union[list], list2: Union[list]) -> Union[list]:
    '''функция, которая получает на вход два списка чисел и возвращает новый
    список, содержащий только те числа, которые встречаются в обоих списках'''
    set1 = set(list1)
    set2 = set(list2)

    # Находим пересечение множеств
    same_numbers = set1.intersection(set2)

    # Возвращаем результат в виде списка
    return list(same_numbers)


# Пример использования:
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
result = find_same_numbers(list_a, list_b)
print(result)  # Вывод: [4, 5]
