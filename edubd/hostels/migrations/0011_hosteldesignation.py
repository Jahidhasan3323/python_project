# Generated by Django 3.0.8 on 2020-08-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0010_hostelroomstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
