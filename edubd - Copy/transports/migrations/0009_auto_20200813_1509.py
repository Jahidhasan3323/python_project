# Generated by Django 3.0.8 on 2020-08-13 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0008_schedulemember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulemember',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transports.Schedule'),
        ),
    ]
