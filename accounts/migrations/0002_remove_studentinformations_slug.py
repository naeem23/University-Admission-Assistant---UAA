# Generated by Django 2.0.6 on 2019-02-28 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinformations',
            name='slug',
        ),
    ]
