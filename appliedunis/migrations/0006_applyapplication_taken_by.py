# Generated by Django 2.0.6 on 2019-05-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliedunis', '0005_remove_applyapplication_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyapplication',
            name='taken_by',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
