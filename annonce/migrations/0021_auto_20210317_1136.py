# Generated by Django 3.1.6 on 2021-03-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0020_auto_20210317_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='accessible_handicape',
            field=models.BooleanField(choices=[(0, 'Oui'), (1, 'Non')], default=1),
        ),
        migrations.AlterField(
            model_name='condition',
            name='animaux_accepte',
            field=models.BooleanField(choices=[(0, 'Oui'), (1, 'Non')], default=1),
        ),
        migrations.AlterField(
            model_name='condition',
            name='fumeur_accepte',
            field=models.BooleanField(choices=[(0, 'Oui'), (1, 'Non')], default=1),
        ),
    ]
