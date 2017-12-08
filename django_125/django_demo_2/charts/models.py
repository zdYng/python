from django.db import models

# Create your models here.
class Chart(models.Model):
    time = models.CharField(max_length=100)
    predict = models.FloatField(max_length=256)

    def __str__(self):
        return self.time
