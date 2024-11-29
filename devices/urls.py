from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('device/<int:pk>/', views.device_detail, name='device_detail'),
    path('category/<int:category_id>/', views.device_by_category, name='device_by_category'),
    path('add/', views.device_create, name='device_create'),
    path('device/<int:pk>/delete/', views.device_delete, name='device_delete'),
    path('device/<int:device_id>/add_review/', views.add_review, name='add_review'),
]