# Generated by Django 2.0.6 on 2019-03-08 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=12, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('seat', models.IntegerField(blank=True, null=True)),
                ('apply_dead', models.DateTimeField()),
                ('apply_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('uni_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universities.University')),
            ],
        ),
    ]
