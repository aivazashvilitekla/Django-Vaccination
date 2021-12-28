from django import forms
import sqlite3
from django.utils.safestring import mark_safe

sqliteConnection = sqlite3.connect('../vacDB.db', check_same_thread=False)
c = sqliteConnection.cursor()
c.execute("select name from regions")

CHOICES = [1, 2]
# for row in c.fetchall():
#     CHOICES.append(row[0])
# 
class VacReg(forms.Form):
    personalNumber = forms.CharField(label=mark_safe('<br/>პირადი ნომერი<br/>'), max_length=11, required=True)
    birthYear = forms.CharField(label=mark_safe('<br/>დაბადების წელი<br/>'), max_length=4, required=True)
    firstname = forms.CharField(label=mark_safe('<br/>სახელი<br/>'), max_length=50, required=True)
    lastname = forms.CharField(label=mark_safe('<br/>გვარი<br/>'), max_length=50, required=True)
    phone = forms.CharField(label=mark_safe('<br/>მობილური<br/>'), max_length=9, required=True)
    email = forms.CharField(label=mark_safe('<br/>ელ-ფოსტა<br/>'), max_length=70, required=False)
    region = forms.ChoiceField(label=mark_safe('<br/>რეგიონი<br/>'), choices=[CHOICES], required=True)
    date = forms.DateTimeField(label=mark_safe('<br/>თარიღი<br/>'), required=True,
        widget=forms.SelectDateWidget)