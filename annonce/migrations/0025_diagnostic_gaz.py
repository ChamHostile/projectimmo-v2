# Generated by Django 3.1.6 on 2021-03-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0024_auto_20210317_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='gaz',
            field=models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=1),
        ),
    ]