from django.db import models

# Create your models here.


class Pizza(models.Model):
    """ Модель пиццы"""
    name = models.CharField(max_length=200)

    """Строковое отображение названий пиццы"""
    def __str__(self):
        return self.name


class Topping(models.Model):
    """Модель топингов для пиццы"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    """Строковое отображение названий топингов"""
    def __str__(self):
        return self.name

