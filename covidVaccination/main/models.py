from django.db import models

# Create your models here.
# class Cities(models.Model):
#     cityID = models.IntegerField(primary_key=True)
#     name = models.TextField()
class VaccineRegistration(models.Model):
    personalID = models.CharField(max_length=11, null=False)
    birthYear = models.CharField(max_length=4)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(null=False, max_length=70)
    phone = models.CharField(null=False, max_length=9)
    email = models.EmailField(null = True, max_length=254)
    regionID = models.IntegerField(null=False)
    time = models.DateField(null=False, auto_now=False, auto_now_add=False)
    vaccineName = models.CharField(null=False, default='', max_length=50)
class Vaccines(models.Model):
    name = models.CharField(null=False, max_length=70)
    quantity = models.IntegerField()

class Cities(models.Model):
    name = models.CharField(null=False, max_length=70)

class Hospitals(models.Model):
    name = models.CharField(null=False, max_length=70)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, default='')

class Regions(models.Model):
    name = models.CharField(null=False, max_length=70)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)