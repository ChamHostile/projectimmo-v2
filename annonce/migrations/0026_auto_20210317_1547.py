# Generated by Django 3.1.6 on 2021-03-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0025_diagnostic_gaz'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='consommationNrj',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='docPerformance',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='emissionGaz',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]