from django.db import models

# Create your models here.
class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    email  =models.EmailField()
    mobile_number = models.IntegerField()