# Generated by Django 2.0.6 on 2019-05-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0029_auto_20190518_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='apply_dead',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
