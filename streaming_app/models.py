from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.FileField()