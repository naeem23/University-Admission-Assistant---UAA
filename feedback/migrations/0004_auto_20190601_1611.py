# Generated by Django 2.0.6 on 2019-06-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='review',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
