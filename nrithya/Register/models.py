from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100)
    first_name = models.TextField(max_length=150)
    username = models.TextField(max_length=150)
    phone = models.TextField()
    password = models.TextField(max_length=15)

    def __str__(self):
        return self.username