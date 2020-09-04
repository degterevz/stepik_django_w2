from data import title, departures


def add_context(request):
    """
    Добавляем направления в контекст для меню
    """
    return {'title': title,
            'departures': departures}
