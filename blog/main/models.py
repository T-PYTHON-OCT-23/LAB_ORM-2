from django.db import models

# Create your models here.
class Post(models.Model):
    categories = models.TextChoices("Categories", ["General", "Caltural", "Horror", "Fantasy","Comedy"])

    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=64, choices=categories.choices, default="General")
    image = models.ImageField(upload_to="blog/images",  default="images/default.png")
    
    def __str__(self):
        return self.title