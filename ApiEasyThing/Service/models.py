from django.db import models
from Company.models import Company
from django.contrib.auth.models import User
from constants import DEFAULT_LOCATION_JSON_OBJECT


class ServiceType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class WorkSchedule(models.Model):
    master = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, default="")
    monday = models.CharField(max_length=255, null=True, blank=True)
    tuesday = models.CharField(max_length=255, null=True, blank=True)
    wednesday = models.CharField(max_length=255, null=True, blank=True)
    thursday = models.CharField(max_length=255, null=True, blank=True)
    friday = models.CharField(max_length=255, null=True, blank=True)
    saturday = models.CharField(max_length=255, null=True, blank=True)
    sunday = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Service(models.Model):
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    company = models.ForeignKey(
        Company, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
    parentService = models.ForeignKey(
        "Service", related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(blank=True, max_length=100, null=True)
    location = models.TextField(
        default=DEFAULT_LOCATION_JSON_OBJECT)
    dateCreated = models.DateField(blank=True, null=True)
    dateRegistration = models.DateField(blank=True, null=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    types = models.ManyToManyField(ServiceType, null=True, blank=True)
    workSchedule = models.OneToOneField(
        WorkSchedule, related_name='workSchedule', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)
