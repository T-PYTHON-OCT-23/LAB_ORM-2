from typing import Any
from django.db import models

# Create your models here.

class Published(models.Model):
    blogs_content = models.TextChoices("blogs_content",['News',"Story","Poetry"])
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateField()
    blog_content =models.CharField(max_length=56,choices = blogs_content.choices, default="Story")
    image = models.ImageField(upload_to="images/",default="images/default.jpg")
    
