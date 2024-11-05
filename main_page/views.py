from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(reguest):
    if reguest.method == "GET":
        return HttpResponse('Имя:Кайрат'
                            'Фамилия:Алтынбеков'
                            'Хобби:Спорт,читать книги и другие активности')

def about_my_pets(reguest):
    if reguest.method == "GET":
        return HttpResponse('Имя:Арчи'
                            "<img src = 'photo_5280534257913162584_y.jpg' >")


def system_time(request):
    now = datetime.now()  # Получение текущего системного времени
    return HttpResponse(f"Текущая дата и время: {now}")