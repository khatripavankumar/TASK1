from django.db import models

# Create your models here.
class Document(models.Model):
    Tile = models.CharField(max_length=150)
    File = models.FileField(upload_to='document/')
    Description = models.TextField()

