# Generated by Django 2.0.6 on 2019-06-19 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0044_auto_20190619_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='postal_code',
        ),
    ]
