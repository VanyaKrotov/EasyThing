from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    dateCreated = models.DateField()
    location = models.CharField(max_length=255)
    dateRegistration = models.DateField()
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class CompanyNews(models.Model):
    company = models.ForeignKey(
        Company, related_name='news', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    article = models.TextField()
    dateCreate = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE)
    permissions = models.IntegerField()

    def __str__(self):
        return str(self.title)
