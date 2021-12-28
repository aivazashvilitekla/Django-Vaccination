from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import sqlite3
from .forms import VacReg

sqliteConnection = sqlite3.connect('../vacDB.db', check_same_thread=False)
c = sqliteConnection.cursor()
# Create your views here.
def index(request):
    c.execute("select name, quantity from vaccines")

    dt = c.fetchall()
    data = {"dt":dt}
    
    return render(request, 'base.html', data)

def reservation(request, vaccine):
    c.execute("select name from regions")

    ls = []
    for row in c.fetchall():
        ls.append(row[0])
    # 
    form = VacReg(request.POST)
    if request.method == "POST" and form.is_valid():
        
        personal_Number = form.cleaned_data["personalNumber"]
        birth_Year = form.cleaned_data["birthYear"]
        first_name = form.cleaned_data["firstname"]
        last_name = form.cleaned_data["lastname"]
        phone_number = form.cleaned_data["phone"]
        emailA = form.cleaned_data["email"]
        regionN = form.cleaned_data["region"]
        dateD = form.cleaned_data["date"]


        sql = ''' INSERT INTO vaccineRegistration(personalID, birthYear, firstname, lastname, phone, email, regionID, time)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
        data_tuple = (
            personal_Number,
            birth_Year,
            first_name,
            last_name,
            phone_number,
            emailA,
            regionN,
            dateD
            )
        c.execute(sql, data_tuple)
        sqliteConnection.commit()
        # if form.is_valid:
        return HttpResponseRedirect('<h1>congrats</h1>')
            
    else:
        form = VacReg()
            

    
    return render(request, 'reservation/reservation.html', {'vaccine': vaccine, "regions": ls, "form": form})