from django.db import models

# Create your models here.
class Blog(models.Model):
        
    categories = models.TextChoices("Categories", ["technology", "movies", "books", "else"])

    title  = models.CharField(max_length=2048)
    content = models.TextField()
    is_published= models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices)
    rating = models.IntegerField()
    poster = models.ImageField(upload_to="img/" , default="img/default.jpg")

