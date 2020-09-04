from random import sample

from django.http import Http404, HttpResponseServerError
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from data import departures, tours
from tours.services import tours_by_departure, info_about_tours


class MainView(View):

    def get(self, request):
        # Выбираем 6 случайных туров и выводим их в карточках на главной странице
        number_card = 6
        tours_rand = {k: tours[k] for k in sample(range(1, len(tours) + 1), k=number_card)}
        return render(request, "index.html", {'tours': tours_rand})


class DepartureView(View):

    def get(self, request, departure):
        tours_ = tours_by_departure(tours, departure)
        if len(tours_) == 0:
            raise Http404

        info_ = info_about_tours(tours_)
        return render(request, "departure.html", {'departure': departure,
                                                  'departure_name': departures[departure],
                                                  'tours': tours_, 'info': info_})


class TourView(View):

    def get(self, request, id):
        if id not in tours.keys():
            raise Http404

        return render(request, "tour.html", {'tour': tours[id],
                                             'departure_name': departures[tours[id]['departure']]})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!')
