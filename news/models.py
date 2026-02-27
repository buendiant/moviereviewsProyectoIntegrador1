from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=True)
    genre = models.CharField(max_length=250, blank=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self): return self.headline