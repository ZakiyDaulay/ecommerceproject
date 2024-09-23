import uuid 
from django.db import models
from django.contrib.auth.models import User


class ProductEntry(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

