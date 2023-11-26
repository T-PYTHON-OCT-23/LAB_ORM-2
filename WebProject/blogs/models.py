from django.db import models


class Blog(models.Model):

    categories = models.TextChoices("Categories", ["Technical", "News", "Marketing", "Entrepreneurship"])


    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=65, choices=categories.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")




