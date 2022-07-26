from django.shortcuts import render

# Create your views here.


def index(request):
    """Домашняя страница приложения Pizzeria"""
    return render(request, 'pizzas/index.html')
