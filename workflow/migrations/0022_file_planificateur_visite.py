# Generated by Django 3.1.6 on 2021-04-22 12:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0021_auto_20210422_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='planificateur_visite',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')], max_length=13, null=True),
        ),
    ]
