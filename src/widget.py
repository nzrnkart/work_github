import re
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number  # Импортируем функции


def mask_card_or_account(text: str) -> str:
    """Обрабатывает текст, маскируя номера карт и счетов."""
    # Проверяем, есть ли слово "Счет" или "Счёт"
    is_account = re.search(r'\bСчет\b|\bСчёт\b', text, re.IGNORECASE)
    # Ищем все цифры подряд
    numbers = re.findall(r'\d+', text)
    if not numbers:
        return text  # Нет чисел — возвращаем как есть

    masked_text = text
    for number in numbers:
        if is_account:
            masked = get_mask_account(number)
        else:
            masked = get_mask_card_number(number)
        # Заменяем первое вхождение числа в тексте на замаскированное
        masked_text = masked_text.replace(number, masked, 1)

    return masked_text


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате ISO в формат "ДД.ММ.ГГГГ".

    :param date_string: строка с датой в формате ISO (например, "2024-03-11T02:26:18.671407")
    :return: строка с датой в формате "ДД.ММ.ГГГГ"
    """
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
