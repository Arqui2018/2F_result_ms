# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20180327_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='monto',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='gol_1',
            new_name='g_local',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='gol_2',
            new_name='g_visit',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='partido_id',
            new_name='match_id',
        ),
    ]
