# Generated by Django 2.0.6 on 2019-06-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190601_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='msg_send_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]
