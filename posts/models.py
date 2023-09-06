from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to="uploads/%Y/%m/%d/", blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
