# Generated by Django 3.0.8 on 2020-08-10 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0002_auto_20200810_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200, null=True)),
                ('history', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostels.HostelType')),
            ],
        ),
    ]
