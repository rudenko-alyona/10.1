def get_mask_card_number(card_number: str) -> str:
    '''Принимает номер карты и возвращает маску'''
    card_number = str(card_number)
    card_mask = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
    return card_mask


print(get_mask_card_number("3216549873216549"))


def get_mask_account(account_number: str) -> str:
    '''Принимает на вход номер счета и возвращает его маску'''
    account_number = str(account_number)
    last_four_digits = account_number[-4:]
    return f"**{last_four_digits}"


print(get_mask_account("98765432198765432198"))
