# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160412_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='visibility',
            field=models.IntegerField(choices=[(0, 'Promote event'), (1, 'Set Up'), (2, 'Service hikers')], default=0),
        ),
    ]