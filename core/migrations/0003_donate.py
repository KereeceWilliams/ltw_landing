# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160331_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=3)),
                ('cardholders_name', models.CharField(max_length=300)),
                ('credit_card_number', models.IntegerField(max_length=12)),
                ('card_cvv', models.IntegerField(max_length=3)),
            ],
        ),
    ]
