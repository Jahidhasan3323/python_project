# Generated by Django 3.0.8 on 2020-08-20 03:18

from django.db import migrations, models
import frontoffice.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0006_auto_20200819_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postaldispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=200, null=True)),
                ('sender', models.CharField(max_length=200, null=True)),
                ('referance', models.CharField(max_length=200, null=True)),
                ('dispatch_date', models.DateField(null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='postal', validators=[frontoffice.models.validate_file])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
