from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        
