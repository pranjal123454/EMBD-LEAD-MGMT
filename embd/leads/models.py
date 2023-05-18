from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
     pass

# Create your models here.
class Lead(models.Model):
    first_name=models.CharField(max_length=20,default="")
    last_name=models.CharField(max_length=20,default="")
    requirement=models.CharField(max_length=20,default="")
    country=models.CharField(max_length=20,default="")
    service_id=models.CharField(max_length=20,default="")
    service_type=models.CharField(max_length=20,default="")
    service_tenure=models.CharField(max_length=20,default="")
    service_active=models.CharField(max_length=20,default="")
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Resource",on_delete=models.CASCADE)
    def __str__(self):
          return f"{self.first_name} {self.last_name}"

class Resource(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     
     def __str__(self):
          return self.user.first_name
     

class Upcoming_Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    lead_description = models.CharField(max_length=100)
    def __str__(self):
          return self.name
    
class LeadAction(models.Model):
    lead = models.ForeignKey(Upcoming_Lead, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    action_date = models.DateTimeField(auto_now_add=True)
    action_notes = models.TextField()     