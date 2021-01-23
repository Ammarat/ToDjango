from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.NullBooleanField(default=True)
    is_favorite  = models.BooleanField(default=False)
    

class Books(models.Model):
   title = models.CharField(max_length=100)
   subtitle = models.CharField(max_length=150)
   desсription = models.CharField(max_length=30)
   price = models.IntegerField()
   genre = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   year = models.DateField()
        
