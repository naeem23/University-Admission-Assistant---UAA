# Generated by Django 2.0.6 on 2019-05-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0036_auto_20190527_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='group',
            new_name='groups',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
