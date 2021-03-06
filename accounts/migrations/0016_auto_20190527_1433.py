# Generated by Django 2.0.6 on 2019-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_userprofile_higher_math'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hsc_board',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('barisal', 'Barisal'), ('chittagong', 'Chittagong'), ('comilla', 'Comilla'), ('dhaka', 'Dhaka'), ('dinajpur', 'Dinajpur'), ('jessore', 'Jessore'), ('rajshahi', 'Rajshahi'), ('sylhet', 'Sylhet')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hsc_group',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('science', 'Science'), ('commerce', 'Commerce'), ('humanities', 'Humanities')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='medium',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('bangla', 'Bangla'), ('english', 'English')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='quota',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('N/A', 'N/A'), ('FFQ', 'FFQ'), ('Tribal', 'Tribal'), ('Disability', 'Disability')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ssc_board',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('barisal', 'Barisal'), ('chittagong', 'Chittagong'), ('comilla', 'Comilla'), ('dhaka', 'Dhaka'), ('dinajpur', 'Dinajpur'), ('jessore', 'Jessore'), ('rajshahi', 'Rajshahi'), ('sylhet', 'Sylhet')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ssc_group',
            field=models.CharField(blank=True, choices=[('----------', '----------'), ('science', 'Science'), ('commerce', 'Commerce'), ('humanities', 'Humanities')], max_length=20, null=True),
        ),
    ]
