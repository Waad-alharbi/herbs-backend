from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Herb(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=255)
    uses = models.CharField(max_length=255) 
    preparation = models.TextField()
    warnings = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def str(self):
        return self.name
