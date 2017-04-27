# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('action_network_id', models.CharField(max_length=255)),
                ('street_address_one', models.CharField(blank=True, max_length=255)),
                ('street_address_two', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', localflavor.us.models.USPostalCodeField(blank=True, default='PA', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('phone_number', localflavor.us.models.PhoneNumberField(blank=True, max_length=20)),
            ],
        ),
    ]
