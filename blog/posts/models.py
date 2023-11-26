from django.db import models

# Create your models here.

class Post(models.Model):

    categories = models.TextChoices("Categories", ["Fashion", "Personal blogs", "Lifestyle", "News blogs","technology"])

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_publishd = models.BooleanField(default=False)
    publishd_at = models.DateTimeField()
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=64, choices= categories.choices, default="Lifestyle")
    


    
    
