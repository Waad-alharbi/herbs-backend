from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Herb(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    uses = models.CharField(max_length=255) 
    preparation = models.TextField()
    warnings = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    



EFFECTIVENESS_CHOICES = [
    ('very_ineffective', 'Very ineffective'),
    ('ineffective', 'Ineffective'),
    ('neutral', 'Neutral'),
    ('effective', 'Effective'),
    ('very_effective', 'Very effective'),
]

class HealthTracker(models.Model):
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    herb_name = models.CharField(max_length=100)
    perceived_effectiveness = models.CharField(max_length=30, choices=EFFECTIVENESS_CHOICES)
    side_effects = models.TextField(blank=True) 
    comment = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.herb_name} - {self.date}'
