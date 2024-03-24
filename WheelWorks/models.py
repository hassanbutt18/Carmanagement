import uuid
from django.db import models
from accounts.models import UserProfile


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    VIN = models.CharField(max_length=17,null=True)
    make = models.CharField(max_length=50,null=True)
    model = models.CharField(max_length=50,null=True)
    year = models.TextField(null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
