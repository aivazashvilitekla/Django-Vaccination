from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="main"),
    path('Reservation/<str:vaccine>', views.reservation, name="vaccine_reservation"),
    path('authentication/login', views.loginPage, name="login"),
    path('authentication/register', views.register, name="register"),
    path('authentication/profile', views.profile, name="profile"),
    path('logout', views.logoutUser, name="logout"),
    path('adminpanel', views.adminPage, name="adminpanel"),
]
