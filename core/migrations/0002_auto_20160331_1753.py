# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 17:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='title',
            new_name='City',
        ),
        migrations.RemoveField(
            model_name='register',
            name='description',
        ),
        migrations.AddField(
            model_name='register',
            name='Country',
            field=models.CharField(default='USA', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Date_of_Birth',
            field=models.CharField(default=datetime.datetime(2016, 3, 31, 17, 51, 21, 658864, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Email',
            field=models.CharField(default=datetime.datetime(2016, 3, 31, 17, 51, 33, 13354, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Emergency_Contact_First_Name',
            field=models.CharField(default=datetime.datetime(2016, 3, 31, 17, 51, 44, 99890, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Emergency_Contact_Last_Name',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Emergency_Contact_Phone_Number',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='First_Name',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Gender',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Last_Name',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Phone_Number',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Shirt_Size',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='State',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Street',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Waiver',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='Zip_Code',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
    ]
