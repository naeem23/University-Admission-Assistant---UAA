# Generated by Django 2.0.6 on 2019-05-30 17:59

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
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=255)),
                ('review', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('oe_very_good', models.BooleanField(default=False)),
                ('oe_good', models.BooleanField(default=False)),
                ('oe_fair', models.BooleanField(default=False)),
                ('oe_poor', models.BooleanField(default=False)),
                ('tr_very_good', models.BooleanField(default=False)),
                ('tr_good', models.BooleanField(default=False)),
                ('tr_fair', models.BooleanField(default=False)),
                ('tr_poor', models.BooleanField(default=False)),
                ('s_very_good', models.BooleanField(default=False)),
                ('s_good', models.BooleanField(default=False)),
                ('s_fair', models.BooleanField(default=False)),
                ('s_poor', models.BooleanField(default=False)),
                ('os_very_good', models.BooleanField(default=False)),
                ('os_good', models.BooleanField(default=False)),
                ('os_fair', models.BooleanField(default=False)),
                ('os_poor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
