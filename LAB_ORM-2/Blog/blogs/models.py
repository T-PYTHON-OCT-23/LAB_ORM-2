from django.db import models

# Create your models here.

class Blog(models.Model):
    categories = models.TextChoices("Categories", ["Political", "Sports", "Social", "Technical"])

    
    title = models.CharField(max_length=2048)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices)
    poster = models.ImageField(upload_to="imgs/" , default="imgs/default.png")

    
    
