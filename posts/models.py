from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    
