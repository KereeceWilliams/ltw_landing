# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_volunteer_visibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('question', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='visibility',
            field=models.IntegerField(choices=[(0, '--Select--'), (1, 'Promote event'), (2, 'Set Up'), (3, 'Service hikers')], default=0),
        ),
    ]
