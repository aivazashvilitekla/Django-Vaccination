from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import VacReg, CreateUserForm
from .models import VaccineRegistration, Vaccines
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    dt = Vaccines.objects.all()
    data = {"dt":dt}
    
    return render(request, 'base.html', data)

def reservation(request, vaccine):
    form = VacReg(request.POST)
    if request.method == "POST":

        obj = VaccineRegistration()
        obj.personalID = request.POST["personalNumber"]
        obj.birthYear = request.POST["birthYear"]
        obj.firstname = request.POST["firstname"]
        obj.lastname = request.POST["lastname"]
        obj.phone = request.POST["phone"]
        obj.email = request.POST["email"]
        obj.regionID = request.POST["region"]
        obj.time = request.POST["date"]
        obj.vaccineName = vaccine
        obj.save()
        
        return HttpResponseRedirect('/Reservation/'+vaccine)
            
    else:
        form = VacReg()
            

    
    return render(request, 'reservation/reservation.html', {'vaccine': vaccine,  "form": form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        request.session['username'] = username

        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'username or password is incorrect')
            # return render(request, 'authentication/login.html', context)
    context = {}
    return render(request, 'authentication/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'authentication/register.html', context)

def profile(request):
    # em = Users.objects.filter(username_gte='tekla').email
    context = {}
    em = User.objects.filter(email='tekla@gmail.com')
    for i in em:
        if i.username:
            context['username'] = i.username
        if i.email:
            context['email'] = i.email
    return render(request, 'profile.html', context)