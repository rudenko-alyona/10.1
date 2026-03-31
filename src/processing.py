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


def sort_by_date(data: list, reverse: bool = True):
    """
    Сортирует список словарей по дате (ключ 'date').
    """

    def parse_date(item: list) -> list:

        date_str = item['date']

        for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%m/%d/%Y', '%Y/%m/%d'):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Неизвестный формат даты: {date_str}")

        return sorted(data, key=parse_date, reverse=reverse)


# Пример данных
    records = [
        {'id': 4142, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 9397, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 5942, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 6150, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]

# Сортировка по убыванию (по умолчанию)
    sorted_desc = sort_by_date(records)
    print("По убыванию:", sorted_desc)

# Сортировка по возрастанию
    sorted_asc = sort_by_date(records, reverse=False)
    print("По возрастанию:", sorted_asc)
