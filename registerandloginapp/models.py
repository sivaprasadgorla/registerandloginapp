from django.db import models
class Reg(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20 ,primary_key=True)
    email=models.EmailField()
    mobile=models.CharField(max_length=13)
    dob=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)

# Create your models here.
