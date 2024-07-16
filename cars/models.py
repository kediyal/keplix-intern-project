from django.db import models
from django.urls import reverse


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
