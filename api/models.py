from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Phonemodel(models.Model):
    name=models.CharField(max_length=200,unique=True,blank=True)
    brand=models.CharField(max_length=200,blank=True)
    price=models.PositiveIntegerField(blank=True)
    release_date=models.DateField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self) :
        return self.name