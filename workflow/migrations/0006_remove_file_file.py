# Generated by Django 3.1.6 on 2021-03-10 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20210310_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='File',
        ),
    ]
