# Generated by Django 3.1.6 on 2021-03-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0010_auto_20210311_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='photos_loyer',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]