# Generated by Django 2.0.6 on 2019-03-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_remove_unit_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='required_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
