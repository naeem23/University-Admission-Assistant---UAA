# Generated by Django 2.0.6 on 2019-06-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0043_remove_rating_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
