from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import CheckboxSelectMultiple
# Create your models here.

class Equipements(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

class Charges(models.Model):
    nom = models.CharField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.nom

class Annonce(models.Model):

    address = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        unique=False
    )
    class TypeHebergement(models.TextChoices):
        Appartemment = 'APPT', _('Appartemment')
        Maison = 'MAIS', _('Maison')
        Studio = 'STUD', _('Studio')
        Autre = 'OTHR', _('Autre')

    hebergement_choice = models.CharField(
        max_length=4,
        choices=TypeHebergement.choices,
        default=TypeHebergement.Appartemment,
        verbose_name="Type d'hébergement"
    )

    class TypeLocation(models.TextChoices):
        logement_entier = 'ENTR', _('Logement entier')
        chambre_privee = 'PRIV', _('Chambre privée')
        chambre_partagee = 'PART', _('Chambre partagée')

    type_location_choices = models.CharField(
        max_length=4,
        choices=TypeLocation.choices,
        default=TypeLocation.logement_entier,
        verbose_name="Location partielle ou totale"
    )

    categorie_logement = models.CharField(max_length=50, blank=True)
    titre_logement = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    nombre_personne = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ],
        blank=True
    )
    pieces_couchage = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        blank=True
    )
    equipements = models.ManyToManyField(Equipements, blank=True)
    charges = models.ManyToManyField(Charges, blank=True)
    dureeLocationMini = models.CharField(blank=True, max_length=50)
    dureeLocationMaxi = models.CharField(blank=True, max_length=50)
    loyer_tc = models.FloatField(max_length=50, blank=True, null=True)
    charges_loyer = models.FloatField(max_length=50, blank=True, null=True)

class ImageLogement(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.annonce.titre_logement