# Generated by Django 2.0.6 on 2019-03-09 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0017_auto_20190309_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='dept_slug',
            new_name='slug',
        ),
    ]
