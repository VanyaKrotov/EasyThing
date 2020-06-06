from django.db import models
from Department.models import Department


class Position(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, related_name="positions", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
