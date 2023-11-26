from django.db import models

class Blog(models.Model):
    categories = models.TextChoices("Categories",["Food","Travel" , "Art" , "News"])

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()
    category = models.CharField(max_length=2048,choices=categories.choices , default="Art")
    image = models.ImageField(upload_to="image/" , default="image/default.jpg")
    