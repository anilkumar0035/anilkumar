from django.db import models

# Create your models here.
class Feedbacform(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField(max_length=200)
    date=models.DateField(max_length=100)
    feedback=models.TextField(max_length=200)
