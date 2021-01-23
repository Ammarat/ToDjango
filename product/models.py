from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.NullBooleanField(default=False)
    is_favorite  = models.BooleanField(default=False) 