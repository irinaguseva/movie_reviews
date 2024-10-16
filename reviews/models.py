from django.db import models

class MovieReview(models.Model):
    text = models.TextField()
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return f"Review: {self.text[:50]}... Rating: {self.rating}"
