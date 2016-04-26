# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160420_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterWaiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiver', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='question',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='contact_us',
            name='phone_number',
            field=models.CharField(default='1', max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='Waiver',
            field=models.CharField(help_text='Text text text text text text text', max_length=300),
        ),
    ]