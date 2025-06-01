from typing import List, Dict, Optional
from datetime import datetime


def filter_by_state(items: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по статусу.

    Args:
        items: Список словарей с операциями.
        state: Статус для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей, где значение ключа "state" равно state.
    """
    return [item for item in items if item.get("state") == state]


def sort_by_date(data: List[Dict], ascending: bool = False) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Args:
        data: Список словарей с операциями, где есть ключ "date" в формате ISO 8601.
        ascending: Указывает порядок сортировки. Если True, сортировка по возрастанию, иначе — по убыванию.

    Returns:
        Новый список словарей, отсортированных по дате.
    """
    def parse_date(item: Dict) -> datetime:
        date_str = item.get("date")
        if date_str:
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                return datetime.min
        return datetime.min

    return sorted(data, key=parse_date, reverse=not ascending)


if __name__ == "__main__":
    operations = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    # Пример работы функции filter_by_state
    filtered_operations_default = filter_by_state(operations)
    print("Фильтрованные операции со статусом по умолчанию 'EXECUTED':")
    print(filtered_operations_default)

    filtered_operations_canceled = filter_by_state(operations, 'CANCELED')
    print("\nФильтрованные операции со статусом 'CANCELED':")
    print(filtered_operations_canceled)

    # Пример работы функции sort_by_date
    sorted_operations_desc = sort_by_date(operations)
    print("\nОтсортированные операции (по убыванию):")
    print(sorted_operations_desc)

    sorted_operations_asc = sort_by_date(operations, ascending=True)
    print("\nОтсортированные операции (по возрастанию):")
    print(sorted_operations_asc)
