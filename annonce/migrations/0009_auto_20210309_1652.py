# Generated by Django 3.1.6 on 2021-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0008_annonce_dureelocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annonce',
            old_name='dureeLocation',
            new_name='dureeLocationMaxi',
        ),
        migrations.AddField(
            model_name='annonce',
            name='dureeLocationMini',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]