from django.urls import path
from .views import (
    car_list_view,
    car_detail_view,
    car_create_view,
    car_delete_view,
    home_view,
)

urlpatterns = [
    path("", car_list_view, name="home"),
    path("cars/", car_list_view, name="car-list"),
    path("cars/new/", car_create_view, name="car-create"),
    path("cars/<int:pk>/", car_detail_view, name="car-detail"),
    path("cars/<int:pk>/delete/", car_delete_view, name="car-delete"),
]
