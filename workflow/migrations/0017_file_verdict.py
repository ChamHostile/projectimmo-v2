# Generated by Django 3.1.6 on 2021-03-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0016_remove_file_verdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='verdict',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
