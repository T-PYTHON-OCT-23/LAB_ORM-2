from django.db import models

# Create your models here.

class Sport(models.Model):

    #choices
    categories = models.TextChoices("Categories", ["Athletics", "Team_sport", "Individual_sport", "Water_sport", "Skiing_sport"])

    name = models.CharField(default="fffffff",max_length=1024)
    description = models.TextField(default="fffffff")
    is_published =models.BooleanField()
    published_at = models.DateField()
    rating = models.IntegerField()
    category = models.CharField(max_length=64, choices=categories.choices,default="Athletics")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
