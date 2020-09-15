from django.db import models

# Create your models here.
class Feed (models.Model) :
    name = models.TextField(max_length=30)
    email = models.EmailField()
    feeds = models.TextField(max_length=200)