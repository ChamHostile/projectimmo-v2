# Generated by Django 3.1.6 on 2021-03-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('s_name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
            ],
        ),
    ]
