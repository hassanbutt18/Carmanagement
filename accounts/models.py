import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    # Personal Information
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              null=True, blank=True)
    address = models.TextField(blank=True,null=True)

    country = models.CharField(max_length=100, blank=True,null=True)
    language = models.CharField(max_length=50, blank=True,null=True)
