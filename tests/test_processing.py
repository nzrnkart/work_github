from src.processing import sort_by_date, sort_by_state


def test_sort_by_date(date_for_sort, date_sorted):
    assert sort_by_date(date_for_sort) == date_sorted


def test_sort_by_state(state_for_sort, state_sorted):
    assert sort_by_state(state_for_sort) == state_sorted
