from django.db import models
from django.contrib.auth.models import User
from Position.models import Position
from User.models import Profile


class WorkHistory(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate = models.DateTimeField(null=True, blank=True)
    position = models.ForeignKey(
        Position, related_name="workers", on_delete=models.CASCADE, blank=True, null=True)
