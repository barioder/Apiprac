# Generated by Django 4.0.6 on 2022-10-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac_app', '0008_phonemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='number_of_buttons',
            field=models.IntegerField(default=5),
        ),
    ]
