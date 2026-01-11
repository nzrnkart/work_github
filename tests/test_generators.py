import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(func_for_usd_and_description, func_usd):
    result6 = list(filter_by_currency(func_for_usd_and_description))
    assert result6 == list(func_usd)


def test_transaction_descriptions(func_for_usd_and_description, func_desc):
    result7 = list(transaction_descriptions(func_for_usd_and_description))
    assert result7 == list(func_desc)


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [  # Список с транзакцией в USD
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {
                        "amount": "67314.70",
                        "currency": {"name": "USD", "code": "USD"},  # Код валюты USD
                    },
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            [  # Ожидаем список с этой транзакцией
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
        ),
        (
            [  # Транзакция НЕ в USD (код RUB)
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},  # Не USD
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            [],  # Ожидаем пустой список
        ),
        (
            [  # Несколько транзакций, только одна в USD
                {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
            ],
            [  # Ожидаем только транзакции с USD
                {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
                {"id": 3, "operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
            ],
        ),
    ],
)
def test_filter_by_currency_parametrized(transactions, expected):
    # Преобразуем результат итератора в список для сравнения
    actual_result = list(filter_by_currency(transactions))
    assert actual_result == expected


def test_basic_range():
    generator = card_number_generator(1, 5)
    result = list(generator)

    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_single_number():
    generator = card_number_generator(9999, 9999)
    result = list(generator)

    expected = ["0000 0000 0000 9999"]
    assert result == expected


def test_large_numbers():
    generator = card_number_generator(9999999999999999, 9999999999999999)
    result = list(generator)

    expected = ["9999 9999 9999 9999"]
    assert result == expected


def test_zero_start():
    generator = card_number_generator(0, 3)
    result = list(generator)

    expected = ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected


@pytest.mark.parametrize(
    "start, stop, expected_first, expected_last, expected_count",
    [
        (1, 10, "0000 0000 0000 0001", "0000 0000 0000 0010", 10),
        (999, 1001, "0000 0000 0000 0999", "0000 0000 0000 1001", 3),
        (0, 0, "0000 0000 0000 0000", "0000 0000 0000 0000", 1),
        (12345678, 12345678, "0000 0000 1234 5678", "0000 0000 1234 5678", 1),
    ],
)
def test_parametrized_ranges(start, stop, expected_first, expected_last, expected_count):
    generator = card_number_generator(start, stop)
    result = list(generator)

    assert len(result) == expected_count
    if expected_count > 0:
        assert result[0] == expected_first
        assert result[-1] == expected_last


def test_overflow_handling():
    # Если передать число больше 9999999999999999
    generator = card_number_generator(10**16, 10**16)  # 10000000000000000

    # Проверяем, как функция обрабатывает это
    result = list(generator)
    # Проверяем, что результат является списком (функция не вызывает ошибок)
    assert isinstance(result, list)
