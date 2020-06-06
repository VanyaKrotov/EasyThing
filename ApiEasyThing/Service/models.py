from django.db import models
from Company.models import Company

class Service(models.Model):
    company = models.ForeignKey(Company, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
    parentService = models.ForeignKey("Service", related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(blank=True, max_length=100, null=True)
    country = models.CharField(max_length=100)
    adress = models.CharField(max_length=255)
    dateCreated = models.DateField(blank=True, null=True)
    dateRegistration = models.DateField(blank=True, null=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    typeId = models.IntegerField()

    def __str__(self):
        return str(self.title)
