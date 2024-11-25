from django.urls import path, include
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('about_my_pet/', views.about_my_pet),
    path('current_time/', views.current_tima),
    path('book/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]














# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib import admin
# from django.urls import path, include
# from main_page import views
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('about_me/', views.about_me, name='about_me'),
#     path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
#     path('system_time/', views.system_time, name='system_time'),
#     path('book/', views.BookListView.as_view(), name='book-list'),
#     path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
#     path('', include('main_page.urls')),
# ]
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,
#                       document_root=settings.STATIC_ROOT)