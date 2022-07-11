from django.db import models

# Create your models here.
class LandLord(models.Model):
    first_name=models.CharField(max_length=20, verbose_name='First Name')
    prof_pic=models.ImageField()