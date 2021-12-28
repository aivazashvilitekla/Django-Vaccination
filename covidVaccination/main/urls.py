from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="main"),
    path('Reservation/<str:vaccine>', views.reservation, name="vaccine_reservation")
]
