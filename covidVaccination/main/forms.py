from django import forms
from django.forms import fields
from django.utils.safestring import mark_safe

from .models import Regions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES = []
regions = Regions.objects.all()
for i in regions:
    CHOICES.append(i.id)
# 
class VacReg(forms.Form):
    personalNumber = forms.CharField(label=mark_safe('პირადი ნომერი'), max_length=11, required=True)
    birthYear = forms.CharField(label=mark_safe('<br/>დაბადების წელი'), max_length=4, required=True)
    firstname = forms.CharField(label=mark_safe('<br/>სახელი'), max_length=50, required=True)
    lastname = forms.CharField(label=mark_safe('<br/>გვარი'), max_length=50, required=True)
    phone = forms.CharField(label=mark_safe('<br/>მობილური'), max_length=9, required=True)
    email = forms.CharField(label=mark_safe('<br/>ელ-ფოსტა'), max_length=70, required=False)
    region = forms.ChoiceField(label=mark_safe('<br/>რეგიონი'), choices=[CHOICES], required=True)
    date = forms.CharField(label=mark_safe('<br/>თარიღი(YYYY-MM-DD)'), required=True)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
