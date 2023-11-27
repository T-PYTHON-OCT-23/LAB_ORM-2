from django.db import models

# Create your models here.
class Blog(models.Model):
    categories=models.TextChoices("categories",["Travel", "Art","Food"])
    title =models.CharField(max_length=256, default="")
    content= models.TextField(default="")
    is_published =models.BooleanField(default=False)
    published_at =models.DateTimeField(null=True , blank=True)
    category=models.CharField(max_length=156,choices=categories.choices, default="")
    image = models.ImageField(upload_to="img/", default="img/default.png")

