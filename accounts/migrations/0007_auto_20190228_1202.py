# Generated by Django 2.0.6 on 2019-02-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190228_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
