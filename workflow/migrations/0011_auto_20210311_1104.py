# Generated by Django 3.1.6 on 2021-03-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_file_verdict'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('s_name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('File', models.FileField(blank=True, upload_to='')),
                ('verdict', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='verdict',
        ),
    ]
