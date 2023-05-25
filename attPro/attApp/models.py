

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
