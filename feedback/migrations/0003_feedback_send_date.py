# Generated by Django 2.0.6 on 2019-06-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20190531_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='send_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
