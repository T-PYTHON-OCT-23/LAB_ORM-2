from django.db import models
 

class Blog1(models.Model):
    categories=models.TextChoices('categories',['Food','Travel','Fashion','Personal'])
    title=models.CharField(max_length=2000)
    content=models.TextField()
    is_published=models.BooleanField()
    published_at=models.DateField()
    category=models.CharField(max_length=200,choices=categories.choices)
    image= models.ImageField(upload_to="images/", default="images/blog.jpeg")
        # Create your models here.
