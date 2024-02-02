import http.client

from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'ПРостой текст о магазине !!!'
    }
    return render(request, 'main/about.html', context)


def shipping_and_payment(request):
    context = {
        'title': 'Доставка и олата',
        'content': 'Информация о доставке и оплате',
    }
    return render(request, 'main/shipping_and_payment.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
        'content': 'Наши контакты',
        'text': 'Номера телефонов 55-55-55'
    }
    return render(request, 'main/contact.html', context)


