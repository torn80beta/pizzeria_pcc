from django.urls import path
from . import views

"""Определение схемы URL для проекта Pizzeria"""
app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
]
