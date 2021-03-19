from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=32)
    data_link = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
