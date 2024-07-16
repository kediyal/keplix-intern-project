from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from .models import Car


# Using Function-Based-Views (FBVs) for now.
# List view for the available cars.
def car_list_view(request):
    context = {
        "cars": Car.objects.all(),
    }
    return TemplateResponse(request, "cars/car_list.html", context)


# Detail view for individual cars.
def car_detail_view(request, pk):
    context = {
        "car": get_object_or_404(Car.objects.all(), pk=pk),
    }
    return TemplateResponse(request, "cars/car_detail.html", context)
