from django.db import models

# Create your models here.
class Profile(models.Model):
   
    
    name=models.CharField(max_length=1000)
    email=models.EmailField()
    phone=models.CharField(max_length=1000)
    summery=models.TextField()
    degree=models.CharField(max_length=300)
    school=models.CharField(max_length=2000)
    university=models.CharField(max_length=500)
    pervious_work=models.TextField(max_length=3000)
    skill=models.TextField(max_length=2000)

    
