from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    """Домашняя страница приложения Pizzeria"""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Вывод списка пицц"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

