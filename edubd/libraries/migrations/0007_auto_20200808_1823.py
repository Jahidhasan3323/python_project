# Generated by Django 3.0.8 on 2020-08-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0006_booklanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklanguage',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
