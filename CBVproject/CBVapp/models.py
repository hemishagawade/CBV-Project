from django.db import models

# Create your models here.

class Student(models.Model):
    # id - auto genenrated
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    perc = models.FloatField()
