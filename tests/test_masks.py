import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6", "1234 56** **** 3456"),
        ("125636232723", "введен некорректный номер карты"),
        ("ivalidsyntaxis", "номер карты должен содержать только цифры"),
        ("12331123123112", "введен некорректный номер карты"),
    ],
)
def test_get_mask_card_number(entry_value, expected):
    assert get_mask_card_number(entry_value) == expected


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("12345678123456789012", "**9012"),
        ("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0", "**7890"),
        ("125636232723", "введен некорректный номер счета"),
        ("ivalidsyntaxis", "номер счета должен содержать только цифры"),
        ("1233112312311212", "введен некорректный номер счета"),
    ],
)
def test_get_mask_account(entry_value, expected):
    assert get_mask_account(entry_value) == expected
