from django.db import models
import datetime
# debut code pour User= Client
from django.contrib.auth.models import User
# fin code pour User= Client

# Create your models here.
class Client(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    nom=models.CharField(max_length=200, null=True)
    telephone=models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
    return self.nom

class Meta:
    managed = True
    db_table = 'client'
    verbose_name = 'Client'