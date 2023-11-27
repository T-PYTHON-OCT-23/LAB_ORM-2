from django.db import models

# Create your models here.

class Blog(models.Model):

    categories = models.TextChoices("Categories", ["Educationl", "Art", "Cultual", "Podcast" ,"Corporate"])
   
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()
    category = models.CharField(max_length=70, choices=categories.choices, default="Cultural" )
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")

