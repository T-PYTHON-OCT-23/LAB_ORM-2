from django.db import models

# Create your models here.

class Info(models.Model):
    categories = models.TextChoices("Categories", ["Comment", "Complaint", "Suggestion"])
    title = models.CharField(max_length=2000)
    contant = models.TextField()
    is_published= models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices,default="Comment")
    poster = models.ImageField(upload_to="images/", default="images/content.jpeg")



