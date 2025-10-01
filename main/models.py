from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('international', 'International'),
        ('national', 'National'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    jersey_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_jersey_hot(self):
        return self.jersey_views > 50 

    def increment_views(self):
        self.jersey_views += 1
        self.save()

