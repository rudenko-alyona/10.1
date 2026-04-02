def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


# Пример данных
transactions = [
     {'id': 4142, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 9397, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 5942, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 6150, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по умолчанию (только 'EXECUTED')
executed_transactions = filter_by_state(transactions)
print(executed_transactions)
# Вывод: [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

# Фильтрация по другому значению
pending_transactions = filter_by_state(transactions, 'PENDING')
print(pending_transactions)
# Вывод: [{'id': 2, 'state': 'PENDING'}]

from datetime import datetime


def sort_by_date(data_list: list, descending: bool =True):
    """
    Сортирует список словарей по ключу 'date'.
    """
    # Преобразуем строковую дату в объект datetime для правильного сравнения
    # Формат даты 'dd.mm.yyyy'
    return sorted(data, key=lambda x: x['date'], reverse=descending)

#Пример использования
data = [
    {'id': 41428829, 'state': 'EXECUTED',
    'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED',
     'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED',
     'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED',
     'date': '2018-10-14T08:21:33.419441'}
]

# Сортировка по убыванию (по умолчанию)
sorted_desc = sort_by_date(data)
print("По убыванию:", sorted_desc)

# Сортировка по возрастанию
sorted_asc = sort_by_date(data, descending=False)
print("По возрастанию:", sorted_asc)

