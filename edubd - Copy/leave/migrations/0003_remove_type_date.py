# Generated by Django 3.0.8 on 2020-08-16 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_auto_20200816_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='date',
        ),
    ]
