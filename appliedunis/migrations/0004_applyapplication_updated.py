# Generated by Django 2.0.6 on 2019-05-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliedunis', '0003_applyapplication_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyapplication',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
