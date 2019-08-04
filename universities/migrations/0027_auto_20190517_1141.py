# Generated by Django 2.0.6 on 2019-05-17 05:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0026_auto_20190506_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='rating',
            new_name='curriculam',
        ),
        migrations.AddField(
            model_name='department',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='credit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='employ_ability',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='extra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='lab',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='quality',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='success',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
