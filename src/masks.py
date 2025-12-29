from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (16 цифр, может содержать пробелы)

    Returns:
        Замаскированный номер карты или строка ошибки
    """
    value = str(card_number).strip()
    cleaned = ''.join(value.split())

    if '*' in cleaned:
        return value

    if not cleaned:
        return "введен некорректный номер карты"

    if not cleaned.isdigit():
        return "номер карты должен содержать только цифры"

    if len(cleaned) != 16:
        return "введен некорректный номер карты"

    # Маскировка: XXXX XX** **** XXXX
    masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"
    return masked


def get_mask_account(card_number: Union[str, int]) -> str:
    """
    Маскирует номер банковского счета в формате **XXXX.

    Args:
        card_number: Номер счета (20 цифр, может содержать пробелы)

    Returns:
        Замаскированный номер счета или строка ошибки
    """
    value = str(card_number).strip()
    cleaned = ''.join(value.split())

    if '*' in cleaned:
        return value

    if not cleaned:
        return "введен некорректный номер счета"

    if not cleaned.isdigit():
        return "номер счета должен содержать только цифры"

    if len(cleaned) != 20:
        return "введен некорректный номер счета"

    # Маскировка: **XXXX
    last_part = cleaned[-4:]
    return "**" + last_part
