import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, card_number", [("1111222233334444", "1111 22** **** 4444"), ("0", "Вы ввели некорректные данные")]
)
def test_get_mask_card_number(value, card_number: str) -> str:
    assert get_mask_card_number(value) == card_number


@pytest.mark.parametrize(
    "value, account_number", [("11112222333344445555", "**5555"), ("0", "Вы ввели некорректные данные")]
)
def test_get_mask_account(value: str, account_number: str) -> str:
    assert get_mask_account(value) == account_number
