# Generated by Django 2.0.6 on 2019-05-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliedunis', '0007_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='user',
            new_name='receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applyapplication',
            name='status',
            field=models.CharField(choices=[('requested', 'Requested'), ('accepted', 'Accepted'), ('processing', 'Processing'), ('completed', 'Completed')], default='Requested', max_length=120),
        ),
    ]
