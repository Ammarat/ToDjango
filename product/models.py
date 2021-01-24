from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.NullBooleanField(default=True)
    is_favorite  = models.BooleanField(default=False)
    
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()

