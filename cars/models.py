import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1886), max_value_current_year]
    )
    price = MoneyField(max_digits=11, decimal_places=2, default_currency="INR")

    # A user can have many-to-one relationship.
    # In simple words, a user on the website can add multiple
    # cars.
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
