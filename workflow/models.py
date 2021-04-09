from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class AdressWorkflow(models.Model):

    rue = models.CharField(blank=True, max_length=20)
    voie = models.CharField(blank=True, max_length=35)
    ville = models.CharField(blank=True, max_length=20)
    region = models.CharField(blank=True, max_length=20)
    zipCode = models.CharField(blank=True, max_length=5)
    pays = models.CharField(blank=True, max_length=20)

class File(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    class PackageChoices(models.TextChoices):
        PACK_DOSSIER = 'PDOS', _('Pack Dossier')
        PACK_VISITES = 'PVST', _('Pack Visite')
        PACK_BASIQUE = 'PBAS', _('Pack Basique')
        PACK_BOOSTER = 'PBST', _('Pack Booster')
        PACK_PREMIUM = 'PPRE', _('Pack Premium')
        PACK_CONCIERGERIE = 'PCNC', _('Pack Conciergerie')

    package_choice = models.CharField(
        max_length=4,
        choices=PackageChoices.choices,
        default=PackageChoices.PACK_DOSSIER,
        verbose_name='Confirmer votre pack'
    )
    personne_foyer = models.IntegerField(blank=True, null=True, verbose_name='Nombre de personnes dans le foyer')
    address = models.OneToOneField(
        AdressWorkflow,
        on_delete=models.CASCADE,
        null=True,
    )

    class SituationMatrimo_choices(models.TextChoices):
        MARRIE = 'MARR', _('Marrié (e)')
        DIVORCE = 'DIVO', _('Divorcé (e)')
        CELIBATAIRE = 'CELI', _('Célibataire')
        SEPARE = 'SEPA', _('Séparé (e)')
        VEUF = 'VEUF', _('Veuf (ve)')

    situation_matrimo = models.CharField(
        max_length=4,
        choices=SituationMatrimo_choices.choices,
        default=SituationMatrimo_choices.CELIBATAIRE,
        verbose_name='Situation matrimoniale'
    )
    referent = models.CharField(max_length=100, blank=True, null=True)
    lieuRecherche = models.CharField(max_length=100, blank=True, null=True)
    typeBien = models.CharField(max_length=100, blank=True, null=True)
    budgetLoyer = models.IntegerField(blank=False, null=True)
    SalaireFoyer = models.IntegerField(blank=False, null=True)
    motifDemenag = models.TextField(max_length=3000, blank=True, null=True)
    precisRecherche = models.TextField(max_length=3000, blank=True, null=True)
    document_avis = models.FileField(blank=True, null=True,
                                     upload_to='documents/',
                                     verbose_name="Pièce 1: Avis d'impot, attestation d'emplyeur ou contrat de travail")
    document_paye = models.FileField(blank=True, null=True,
                                     upload_to='documents/',
                                     verbose_name="Pièce 2: 3 dernières fiches de payes, pièces d'identité")
    document_quittance = models.FileField(blank=True, null=True,
                                          upload_to='documents/',
                                          verbose_name="Pièce 3: 3 dernières quittance de loyers")

    class Verdict_choice(models.TextChoices):
        accepte = 'acct', _('Accepté')
        attente = 'attn', _('Attente')
        refuse = 'refu', _('Refusé')


    verdict = models.CharField(
        max_length=4,
        choices=Verdict_choice.choices,
        default=Verdict_choice.refuse,
        verbose_name='Verdict'
    )


