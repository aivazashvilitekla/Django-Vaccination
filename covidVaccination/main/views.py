from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
import sqlite3
from .forms import VacReg
from .models import VaccineRegistration, Vaccines

# Create your views here.
def index(request):
    dt = Vaccines.objects.all()
    data = {"dt":dt}
    
    return render(request, 'base.html', data)

def reservation(request, vaccine):
    form = VacReg(request.POST)
    if request.method == "POST":
        personal_Number = request.POST["personalNumber"]
        birth_Year = request.POST["birthYear"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        phone_number = request.POST["phone"]
        emailA = request.POST["email"]
        regionN = request.POST["region"]
        dateD = request.POST["date"]

        obj = VaccineRegistration()
        obj.personalID = personal_Number
        obj.birthYear = birth_Year
        obj.firstname = first_name
        obj.lastname = last_name
        obj.phone = phone_number
        obj.email = emailA
        obj.regionID = regionN
        obj.time = dateD
        obj.vaccineName = vaccine
        obj.save()
        
        return HttpResponseRedirect('/Reservation/'+vaccine)
            
    else:
        form = VacReg()
            

    
    return render(request, 'reservation/reservation.html', {'vaccine': vaccine,  "form": form})

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    return render(request, 'authentication/register.html')