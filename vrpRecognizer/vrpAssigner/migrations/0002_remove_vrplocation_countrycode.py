# Generated by Django 3.1.2 on 2020-12-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vrpAssigner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vrplocation',
            name='countryCode',
        ),
    ]
