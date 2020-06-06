from django.db import models
from Company.models import Company
from Service.models import Service


class Department(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company, related_name='company',
                                on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='service',
                                on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
