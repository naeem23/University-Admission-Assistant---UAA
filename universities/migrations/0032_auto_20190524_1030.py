# Generated by Django 2.0.6 on 2019-05-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0031_auto_20190523_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='seat',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
