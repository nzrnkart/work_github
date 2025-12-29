from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_card_or_account

print(get_mask_card_number("1234567812345678"))
print(get_mask_account("123456"))

print(mask_card_or_account("Visa Platinum 7000792289606361"))
print(mask_card_or_account("Счет 73654108430135874305"))


if __name__ == "__main__":
    date_input = "2024-03-11T02:26:18.671407"
    formatted_date = get_date(date_input)
    print(formatted_date)
