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

def pizza(request, pizza_id):
    """Вывод пиццы со всеми топингами"""
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'entries': entries}
    return render(request, 'pizzas/pizza.html', context)
