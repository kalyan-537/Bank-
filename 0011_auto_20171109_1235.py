# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0010_auto_20171109_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='c_id',
            new_name='d_id',
        ),
    ]
