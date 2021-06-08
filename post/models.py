from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

# Create your models here.
