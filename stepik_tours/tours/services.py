def tours_by_departure(tours: dict, departure: str) -> dict:
    """
    Функция отбирает туры из общего списка по направлению departure
    """
    tours_departure = {}

    for id, tour in tours.items():
        if tour['departure'] == departure:
            tours_departure[id] = tour

    return tours_departure


def info_about_tours(tours: dict) -> dict:
    """
    Функция возвращает словарь с максимальными/минимальными стоимостью и количестве ночей
    среди всех переданных в нее туров. А так же общее количество туров
    """
    nights = []
    prices = []

    for id, tour in tours.items():
        nights.append(tour['nights'])
        prices.append(tour['price'])

    nights.sort()
    prices.sort()

    min_nights, max_nights = 0, 0
    min_price, max_price = 0, 0

    if len(nights) > 0:
        min_nights, max_nights = nights[0], nights[-1]

    if len(prices) > 0:
        min_price, max_price = prices[0], prices[-1]

    return {'min_nights': min_nights, 'max_nights': max_nights,
            'min_price': min_price, 'max_price': max_price, 'count': len(tours)}
