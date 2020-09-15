from django.db import models

# Create your models here.

class Work (models.Model) :
    name = models.TextField(max_length=30)
    email = models.EmailField()
    gender = models.TextField(max_length=30)
    phone = models.TextField()
    birthday = models.TextField(max_length=30)
    experience = models.TextField(max_length=30)
    years = models.TextField(max_length=30)
    months = models.TextField(max_length=30)
    currentsalary = models.TextField(max_length=30)
    expectedsalary = models.TextField(max_length=30)
    nameofdegree = models.TextField(max_length=30)
    passyear = models.TextField(max_length=30)
    formsknown = models.TextField(max_length=100)