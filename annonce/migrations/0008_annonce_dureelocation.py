# Generated by Django 3.1.6 on 2021-03-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0007_auto_20210308_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='dureeLocation',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
