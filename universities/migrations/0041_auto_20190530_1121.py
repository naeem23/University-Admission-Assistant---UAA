# Generated by Django 2.0.6 on 2019-05-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0040_auto_20190529_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='required_gpa',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='required_gpa_each',
        ),
        migrations.AlterField(
            model_name='unit',
            name='apply_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
