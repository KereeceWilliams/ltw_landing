# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_donate_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='donate',
            name='card_cvv',
        ),
        migrations.RemoveField(
            model_name='donate',
            name='cardholders_name',
        ),
        migrations.RemoveField(
            model_name='donate',
            name='credit_card_number',
        ),
        migrations.RemoveField(
            model_name='donate',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='register',
            name='card_cvv',
        ),
        migrations.RemoveField(
            model_name='register',
            name='cardholders_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='credit_card_number',
        ),
        migrations.RemoveField(
            model_name='register',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='card_cvv',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='credit_card_number',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='expiration_date',
        ),
    ]