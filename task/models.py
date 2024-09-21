from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('INP', 'In Process'),
        ('DONE', 'Done'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.text[:10]} - {self.status}"
    