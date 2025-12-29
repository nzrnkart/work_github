def sort_by_date(transactions: list[dict[str,any]], reverse: bool = True) -> list[dict[str,any]]:
    """
    Функция обрабатывает список словарей от ближайшей даты до самой старой.
    :param transactions: список из ключей и значений(any).
    :param reverse: False, чтобы самые близкие даты к настоящему стояли впереди, а старые - сзади.
    :return: новый список словарей отсортированный по "date"
    """
    return sorted(transactions, key=lambda x:x.get("date"),reverse=reverse)


def sort_by_state(transactions: list[dict[str,any]], state = "EXECUTED") -> list[dict[str,any]]:
    """
    Функция обрабатывает список словарей по принципу: создает новый список словарей с одними и теми же "state".
    :param transactions: список из словарей ключ-значение
    :param state: ключ по умолчанию "EXECUTED"
    :return: возвращает отсортированный список по данному ключу, условленному 2-м параметром в функции.
    """
    new_list = []
    for transaction in transactions:
        if transaction.get("state") == state:
            new_list.append(transaction)
    return new_list