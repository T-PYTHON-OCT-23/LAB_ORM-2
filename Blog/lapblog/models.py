from django.db import models

# Create your models here.
class Web (models.Model):
   categories = models.TextChoices("Categories", ["Vlog", "Photoblog", "Blognews", "Personal blog"])
   Title = models.CharField(max_length=2048) 
   Contant =models.TextField()
   is_published =models.BooleanField()
   published_at = models.DateTimeField()
   category = models.CharField(max_length=64, choices=categories.choices , default="Vlog")
   poster = models.ImageField(upload_to="images/", default="images/r5.JPG")