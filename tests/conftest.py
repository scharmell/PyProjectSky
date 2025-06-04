import pytest


@pytest.fixture
def card_number():
    return "1111 22** **** 4444"


@pytest.fixture
def account_number():
    return "**5555"


@pytest.fixture
def card_widget():
    return "Visa Platinum 8990922113665229"


@pytest.fixture
def account_widget():
    return "Счет 73654108430135874305"

@pytest.fixture
def gen_filter_currency():
    return {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
