from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birthDate = models.DateField()
    telephone = models.CharField(max_length=20)
    privateKey = models.CharField(max_length=64)

    def __str__(self):
        return str(self.telephone)
