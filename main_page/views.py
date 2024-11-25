from django.shortcuts import render, HttpResponse
import datetime
from django.views import generic
from . import models


def about_me(request):
    return render(request, 'main_page/about_me.html')


def about_my_pet(request):
    return HttpResponse(f"Its my cat - Murrr")


def current_tima(request):
    return HttpResponse(datetime.datetime.now())


class BookListView(generic.ListView):
    template_name = 'main_page/book.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'main_page/book_detail.html'
    model = models.Book
    context_object_name = 'book'

def get_queryset(self):
         return models.Book.objects.all()




# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
# from django.views import generic
# from django.shortcuts import get_object_or_404
# from . import models
#
#
# class BookListView(generic.ListView):
#     template_name = 'main_page/book.html'
#     context_object_name = 'books'
#     model = models.Book
#
#     def get_queryset(self):
#         return models.Book.objects.all()
#
#
# class BookDetailView(generic.DetailView):
#     template_name = 'main_page/book_detail.html'
#     context_object_name = 'book'
#     model = models.Book
#
#     def get_queryset(self):
#         return models.Book.objects.all()
#
# def about_me(reguest):
#     if reguest.method == "GET":
#         return HttpResponse('Имя:Кайрат'
#                             'Фамилия:Алтынбеков'
#                             'Хобби:Спорт,читать книги и другие активности')
#
# def about_my_pet(reguest):
#     if reguest.method == "GET":
#         return HttpResponse('Имя:Арчи'
#                             "<img src = 'photo_5280534257913162584_y.jpg' >")
#
#
# def current_time(request):
#     now = datetime.now()  # Получение текущего системного времени
#     return HttpResponse(f"Текущая дата и время: {now}")



