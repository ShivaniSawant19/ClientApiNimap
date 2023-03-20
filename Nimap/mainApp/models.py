from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    AssignTo = models.TextField(max_length=100, blank=True)
    Completed = models.BooleanField(blank=False)
    
def __str__(self):
    return self.Title



