# Generated by Django 3.0.8 on 2020-08-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0006_auto_20200810_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hostel',
            field=models.ManyToManyField(blank=True, to='hostels.Hostel'),
        ),
    ]