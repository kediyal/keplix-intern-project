from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Car


# Using Function-Based-Views (FBVs) for now.
# List view for the available cars.
def car_list_view(request):
    context = {
        "cars": Car.objects.all(),
    }
    return TemplateResponse(request, "cars/car_list.html", context)
