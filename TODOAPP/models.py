from django.db import models


# Create your models here.
class AddTaskModel(models.Model):
    Task = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Due_date = models.CharField(max_length=200)
    Status = models.CharField(max_length=200, default='ToDo')

