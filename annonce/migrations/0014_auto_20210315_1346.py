# Generated by Django 3.1.6 on 2021-03-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0013_calendrier'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendrier',
            name='calendrier_fin',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='calendrier',
            name='caledrier_debut',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]