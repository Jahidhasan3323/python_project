# Generated by Django 3.0.8 on 2020-08-16 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_auto_20200816_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='apply_status',
            new_name='status',
        ),
    ]
