# Generated by Django 4.0.6 on 2022-08-24 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac_app', '0002_rename_surname_name_ppagent_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_fare', models.DecimalField(decimal_places=3, max_digits=11, validators=[django.core.validators.MinValueValidator(0)])),
                ('cancellation_fee', models.DecimalField(decimal_places=3, max_digits=11)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'pricing model',
            },
        ),
    ]
