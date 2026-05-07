from datetime import datetime

from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_string: str) -> str:
    '''Принимает тип и номер карты или счета, возвращает маску'''

    if account_string.startswith("Счет"):  # обработка случая банковского счёта
        _, account_number = account_string.split(maxsplit=1)
        return f"Счет {get_mask_account(account_number)}"
    else:  # обработка всех остальных случаев (карты)
        card_type, card_number = account_string.rsplit(maxsplit=1)
        masked_number = get_mask_card_number(card_number)
        return f"{card_type} {masked_number}"

# Пример для счета:
test1 = "Счет 73654108430135874305"
result1 = mask_account_card(test1)
print(f"Вход:  {test1}")
print(f"Выход: {result1}")

# Пример для карты:
test2 = "Visa Platinum 8990922113665229"
result2 = mask_account_card(test2)
print(f"Вход:  {test2}")
print(f"Выход: {result2}")


def get_date(iso_date_str: str) -> str:
    """Преобразует дату из формата ISO8601 в формат 'DD.MM.YYYY'"""
    # Отбрасываем лишнюю информацию после секунды (.671407)
    cleaned_iso_date = iso_date_str.split('.')[0]
    # Парсим строку в объект datetime
    date_obj = datetime.strptime(cleaned_iso_date, "%Y-%m-%dT%H:%M:%S")
    # Возвращаем строку с датой в нужном формате
    return date_obj.strftime("%d.%m.%Y")

data = get_date("2024-03-11T02:26:18.671407")
print(f"Дата: {data}")
