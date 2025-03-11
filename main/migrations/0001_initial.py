# Generated by Django 5.1.6 on 2025-03-05 02:43

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namemodel', models.CharField(max_length=10)),
                ('emailmodel', models.EmailField(max_length=254, unique=True)),
                ('phonemodel', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('messagemodel', models.TextField()),
            ],
        ),
    ]
