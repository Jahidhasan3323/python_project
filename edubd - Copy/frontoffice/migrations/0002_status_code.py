# Generated by Django 3.0.8 on 2020-08-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]
