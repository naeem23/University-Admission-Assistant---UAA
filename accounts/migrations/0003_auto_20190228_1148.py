# Generated by Django 2.0.6 on 2019-02-28 05:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_remove_studentinformations_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentInformations',
            new_name='StudentInformation',
        ),
    ]
