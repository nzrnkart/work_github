import pytest
from processing import filter_by_state, sort_by_date  # Импорт функций из твоего файла processing.py


# Фикстура для базовых тестовых данных (список операций)
@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-03T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-02T14:00:00"},
        {"id": 4, "state": "PENDING", "date": "2023-01-03T10:00:00"},  # Та же дата, как у id 1
    ]


# Фикстура для пустого списка (edge case)
@pytest.fixture
def empty_operations():
    return []


# Тесты для filter_by_state с параметризацией
@pytest.mark.parametrize("state, expected_ids", [
    # Нормальные случаи
    ("EXECUTED", [1, 3]),  # По умолчанию и custom статус
    ("CANCELED", [2]),
    ("PENDING", [4]),
    # Edge cases
    ("UNKNOWN", []),  # Ни один не подходит
    ("EXECUTED", [1, 3]),  # Все подходят (повтор для проверки)
])
def test_filter_by_state(sample_operations, state, expected_ids):
    original = sample_operations.copy()  # Сохраняем копию для проверки неизменности
    if state == "EXECUTED" and len(expected_ids) == 0:  # Для default case
        result = filter_by_state(sample_operations)
    else:
        result = filter_by_state(sample_operations, state)

    # Проверка результата
    assert [op["id"] for op in result] == expected_ids
    # Проверка неизменности оригинала
    assert sample_operations == original


# Тесты для edge cases filter_by_state
def test_filter_by_state_empty_list(empty_operations):
    result = filter_by_state(empty_operations)
    assert result == []


def test_filter_by_state_missing_state_key(sample_operations):
    # Добавляем элемент без "state"
    operations_with_missing = sample_operations + [{"id": 5, "date": "2023-01-05"}]
    result = filter_by_state(operations_with_missing, "EXECUTED")
    # Предполагаем, что функция игнорирует элементы без "state" (или обрабатывает как не подходящие)
    assert [op["id"] for op in result] == [1, 3]  # Только те с "state" == "EXECUTED"


# Тесты для sort_by_date с параметризацией
@pytest.mark.parametrize("ascending, expected_ids", [
    # Нормальные случаи
    (False, [1, 4, 3, 2]),  # новые даты первыми, стабильная сортировка для одинаковых дат
    (True, [2, 3, 1, 4]),  # старые даты первыми
    # Edge cases
    (False, [1, 4, 3, 2]),  # Повтор для проверки
])
def test_sort_by_date(sample_operations, ascending, expected_ids):
    original = sample_operations.copy()
    result = sort_by_date(sample_operations, ascending=ascending)

    # Проверка результата
    assert [op["id"] for op in result] == expected_ids
    # Проверка неизменности оригинала
    assert sample_operations == original


# Тесты для edge cases sort_by_date
def test_sort_by_date_empty_list(empty_operations):
    result = sort_by_date(empty_operations)
    assert result == []


def test_sort_by_date_same_dates():
    # Все даты одинаковые — порядок должен сохраниться (стабильная сортировка)
    same_date_ops = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2, "date": "2023-01-01T00:00:00"},
    ]
    result = sort_by_date(same_date_ops)
    assert [op["id"] for op in result] == [1, 2]  # Порядок не меняется


def test_sort_by_date_invalid_date(sample_operations):
    # Неправильный формат даты — функция использует fallback (минимальная дата)
    invalid_ops = sample_operations + [{"id": 5, "date": "invalid-date"}]
    result = sort_by_date(invalid_ops)
    assert result[-1]["id"] == 5  # Элемент с invalid датой в конце


def test_sort_by_date_missing_date_key(sample_operations):
    # Элемент без "date" — функция обрабатывает как минимальную дату
    missing_date_ops = sample_operations + [{"id": 6, "state": "EXECUTED"}]
    result = sort_by_date(missing_date_ops)
    assert result[-1]["id"] == 6  # В конце
