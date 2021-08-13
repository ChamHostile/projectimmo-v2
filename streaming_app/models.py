from django.db import models
from django.conf import settings


# Create your models here.
class Video(models.Model):
    name = models.FileField(upload_to='streaming/', blank=True)
    file_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        unique=False
    )