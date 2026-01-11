from typing import Any, Generator, Iterator


def filter_by_currency(iterations: list[Any]) -> Iterator[Any]:
    """
    Функция обрабатывает список словарей по ключу "code" и значению "USD"
    :param iterations: список словарей(также присутствуют списки внутри списка)
    :return: итератор по данным спискам
    """
    for iteration in iterations:
        if iteration.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
            yield iteration


def transaction_descriptions(somethings: list[Any]) -> Iterator[str]:
    """
    Функция проходит по словарю и по ключу "description" отдаёт соответствующее значение.
    :param somethings: список словарей(также присутствуют списки внутри списка).
    :return: итератор возвращает значение по ключу "description".
    """
    for some in somethings:
        yield some.get("description", "описание не найдено")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Функция(генератор) будет возвращать строку из 16 символов-цифр,
    разбитую по 4 символа, разделитель - пробел.
    :param start: начальное значение.
    :param stop: конечное значение.
    :return: начиная с первого по последний+1 элемент цикла,
             возвращает каждый элемент в виде "0000 0000 0000 0001"
    """
    for x in range(start, stop + 1):
        letter: str = f"{x:0>16}"
        last_result: str = " ".join([letter[i : i + 4] for i in range(0, 16, 4)])
        yield last_result
