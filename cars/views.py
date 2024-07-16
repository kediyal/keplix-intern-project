from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy

from .forms import CarForm
from .models import Car


# Using Function-Based-Views (FBVs) for now.
def home_view(request):
    return HttpResponseRedirect("cars/")


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


# Create view for creating new cars.
def car_create_view(request):
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            car = form.save(commit=False)
            car.author = request.user
            car.save()
            return HttpResponseRedirect(reverse("car-detail", kwargs={"pk": car.pk}))
    else:
        form = CarForm()

    context = {
        "form": form,
    }
    return render(request, "cars/car_create.html", context)


# Delete view for deleting existing cars.
def car_delete_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    print(f"Car object: {car}")
    if request.method == "POST":
        car.delete()
        return HttpResponseRedirect(reverse_lazy("home"))
    context = {
        "car": car,
    }
    return TemplateResponse(request, "cars/car_delete.html", context)
