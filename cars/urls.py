from django.urls import path
from .views import car_list_view, car_detail_view, home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("cars/", car_list_view, name="car-list"),
    path("<int:pk>/", car_detail_view, name="car-detail"),
]
