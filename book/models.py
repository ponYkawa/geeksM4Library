from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    cover_url = models.URLField(blank=True)

    def __str__(self):
        return self.title