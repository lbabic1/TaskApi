from django.db import models
import datetime

now = datetime.datetime.now()

# Create your models here.
class Player(models.Model):
    PlayerId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    CurrentClub = models.CharField(max_length=20)
    nationallity = models.CharField(max_length=20)
    DateOfBirth = models.DateField()
    Position = models.CharField(max_length=20)
    LastModified = models.DateTimeField(auto_now=True)
