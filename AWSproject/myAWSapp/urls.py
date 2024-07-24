from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_car, name='edit_car'),
    path('delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('car/<int:pk>/', views.car_detail, name='car_detail')
]
