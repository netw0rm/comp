# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'verbose_name': '配件表', 'verbose_name_plural': '配件表'},
        ),
        migrations.AlterModelTable(
            name='part',
            table='restsv_parts',
        ),
    ]
