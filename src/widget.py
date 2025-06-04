from src.masks import get_mask_account, get_mask_card_number


def get_date(date: str) -> str:
    """Функция работы с данными"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"


def mask_account_card(number: str) -> str:
    """Функция маскировки"""
    list_number = number.split()
    number_card = list_number.pop()
    name_card = " ".join(list_number)
    if name_card == "Счет":
        return f"Счет {get_mask_account(number_card)}"
    else:
        return f"{name_card} {get_mask_card_number(number_card)}"


print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))
