# Generated by Django 3.1.6 on 2021-05-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0035_services_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='annonce',
            name='categorie_service',
            field=models.ManyToManyField(blank=True, to='annonce.CategorieService'),
        ),
    ]
