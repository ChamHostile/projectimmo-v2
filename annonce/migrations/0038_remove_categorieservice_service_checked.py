# Generated by Django 3.1.6 on 2021-05-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0037_categorieservice_service_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorieservice',
            name='service_checked',
        ),
    ]
