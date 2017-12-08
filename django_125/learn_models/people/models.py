from django.db import models

# Create your models here.
class Person(models.Model):
    time = models.CharField(max_length=30)
    predict = models.IntegerField()
    