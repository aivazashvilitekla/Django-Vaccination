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

        a = Vaccines.objects.get(name=vaccine)
        a.quantity -= 1 
        a.save()
        obj.save()
        
        return HttpResponseRedirect('/Reservation/'+vaccine)
            
    else:
        form = VacReg()
            

    
    return render(request, 'reservation/reservation.html', {'vaccine': vaccine,  "form": form})

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)
        if user is not None:
            adminUser = User.objects.get(username=username)
            if adminUser.is_staff==1:
                return redirect('adminpanel/home')

            login(request, user)
            request.session['username'] = username
            context['user'] = user
            return redirect('profile')
        else:
            messages.info(request, 'username or password is incorrect')
            # return render(request, 'authentication/login.html', context)
        
    return render(request, 'authentication/login.html', context)
def logoutUser(request):
    logout(request)
    if 'username' in request.session:
        del request.session['username']
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
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'authentication/register.html', context)

def profile(request):
    # em = Users.objects.filter(username_gte='tekla').email
    context = {}
    if request.session.get('username') is not None:
        em = User.objects.filter(username=request.session.get('username'))
        for i in em:
            if i.username:
                context['username'] = i.username
            if i.email:
                context['email'] = i.email
    else:
        return redirect('login')
    return render(request, 'profile.html', context)
def adminPage(request):
    context = {
        'vaccinesData' : Vaccines.objects.all()
    }
    # a = Vaccines.objects.get(id=5)
    # a.entry_set.set([e1, e2])
    # a.entry_set.set([e1.pk, e2.pk])
    return render(request, 'adminpage.html', context)