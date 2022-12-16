from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text[:70]

    def __str__(self):
        return self.title