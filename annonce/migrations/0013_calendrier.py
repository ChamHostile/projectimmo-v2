# Generated by Django 3.1.6 on 2021-03-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0012_auto_20210312_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caledrier_debut', models.DateField()),
                ('disponibilité', models.CharField(choices=[('disp', 'Disponible'), ('indp', 'Indisponible')], default='disp', max_length=4, verbose_name='Disponibilité')),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annonce.annonce')),
            ],
        ),
    ]