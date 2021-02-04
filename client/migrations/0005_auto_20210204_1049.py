# Generated by Django 3.1.6 on 2021-02-04 10:49

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('client', '0004_auto_20210204_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='locality',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='states', to='address.address'),
        ),
    ]
