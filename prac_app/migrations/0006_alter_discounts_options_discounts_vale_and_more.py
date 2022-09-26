# Generated by Django 4.0.6 on 2022-09-26 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac_app', '0005_discounts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discounts',
            options={'verbose_name_plural': 'Discounts'},
        ),
        migrations.AddField(
            model_name='discounts',
            name='vale',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discounts',
            name='rate',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
