# Generated by Django 3.1.6 on 2021-03-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210318_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='code_postal',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
