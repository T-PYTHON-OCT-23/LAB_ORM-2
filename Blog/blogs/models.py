from django.db import models


class Blog(models.Model):
    
    categories=models.TextChoices("Categories", ["Makeup", "Movie","Celebrities", "Care","Places"])
  

    title=models.CharField(max_length=100)
    content=models.TextField()
    is_published=models.BooleanField()
    published_at=models.DateField()
    category=models.CharField(max_length=50,choices=categories.choices, default="Movie")
    poster = models.ImageField(upload_to="images/", default="images/blog.jpg")