# Generated by Django 4.0.6 on 2022-10-26 12:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('prac_app', '0007_rename_discounts_discountsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('phone_name', models.CharField(max_length=30)),
                ('make', models.CharField(max_length=30)),
            ],
        ),
    ]