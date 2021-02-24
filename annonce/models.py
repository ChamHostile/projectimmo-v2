from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings
# Create your models here.

class Annonce(models.Model):
    address = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE
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

    categorie_logement = models.CharField(max_length=50)