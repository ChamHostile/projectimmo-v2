# Generated by Django 3.1.6 on 2021-04-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0019_auto_20210409_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='type_visite',
            field=models.CharField(max_length=30, null=True),
        ),
    ]