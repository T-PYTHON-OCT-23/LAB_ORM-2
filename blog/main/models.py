from django.db import models
from datetime import date


# Create your models here.


class Blog(models.Model):
    categories = models.TextChoices(
        "Categories", ["Coffee", "Tea", "Matcha", "Water"])

    name = models.CharField(max_length=512)
    paragraph = models.TextField(default='--')
    release_date = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=2048, choices=categories.choices, default="Coffee")
    image = models.ImageField(upload_to="image/", default="image/default.jpg")
