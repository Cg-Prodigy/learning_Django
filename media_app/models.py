from datetime import datetime
from django.db import models

# utility functions
def generate_folder(instance,filename):
    date_time=datetime.now().strftime("%Y%m")
    return "{}/{}/{}".format(date_time,instance.username,filename)
# Create your models here.
class LandLord(models.Model):
    first_name=models.CharField(max_length=20, verbose_name='First Name')
    prof_pic=models.ImageField()

class Tenant(models.Model):
    first_name=models.CharField(max_length=20,verbose_name="First Name")
    last_name=models.CharField(max_length=20, verbose_name='Last Name')
    username=models.CharField(unique=True, max_length=15)
    profile_pic=models.FileField(upload_to=generate_folder)