from django.db import models
from datetime import datetime
from django.utils import timezone
# import uuid


from userapp.models import User


class Project(models.Model):
    # uuid =
    name = models.CharField(max_length=32)
    data_link = models.CharField(max_length=64)
    user = models.ManyToManyField(User)


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
