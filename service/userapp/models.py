from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=32, unique=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    is_superuser = models.BooleanField(default=False)



