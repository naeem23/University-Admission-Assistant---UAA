# Generated by Django 2.0.6 on 2019-02-28 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=255, null=True)),
                ('rocket_number', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user/image')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='user/signature')),
                ('quota', models.CharField(blank=True, max_length=255, null=True)),
                ('medium', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_roll', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_reg', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_pass_y', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_board', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_group', models.CharField(blank=True, max_length=255, null=True)),
                ('ssc_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hsc_roll', models.CharField(blank=True, max_length=255, null=True)),
                ('hsc_reg', models.CharField(blank=True, max_length=255, null=True)),
                ('hsc_pass_y', models.CharField(blank=True, max_length=255, null=True)),
                ('hsc_board', models.CharField(blank=True, max_length=255, null=True)),
                ('hsc_group', models.CharField(blank=True, max_length=255, null=True)),
                ('hsc_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
    ]
