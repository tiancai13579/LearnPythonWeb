from django.db import models

# Create your models here.
class People(models.Model):#都要继承这个
    name = models.CharField(null=True,blank=True,max_length=200)
    job = models.CharField(null=True,blank=True,max_length=200)
