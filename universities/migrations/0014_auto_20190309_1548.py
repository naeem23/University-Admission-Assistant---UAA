# Generated by Django 2.0.6 on 2019-03-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0013_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
