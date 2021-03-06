# Generated by Django 2.0.6 on 2019-06-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0052_auto_20190619_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='arts_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='arts_tgpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='ban_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='bio_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='chem_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='commerce_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='commerce_tgpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='en_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='math_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='phy_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='science_gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='science_tgpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='tgpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
