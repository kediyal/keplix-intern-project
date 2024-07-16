from django.urls import path
from .views import car_list_view

urlpatterns = [
    path("", car_list_view, name="home"),
]
