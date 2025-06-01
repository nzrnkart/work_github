def filter_by_state(items: list, states: list = None) -> list:
    """ Функция фильтрует входящий список словарей по ключу и возвращает новый список словарей,
     в которых есть ключ, соответсвующий указанному значению 'state' """
    if states is None:
        states = ['EXECUTED', 'CANCELED']
    return [item for item in items if item.get('state') in states]

def sort_by_date(data: list) -> list:
    """ Функция принимает список словарей и возвращает новый список отсортированный по дате (по убыванию) """
    return sorted(data, key=lambda x: x.get('date'), reverse=True)

result_1 = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(result_1)

result_2 = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(result_2)