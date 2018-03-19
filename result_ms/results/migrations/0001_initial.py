# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(unique=True)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('gol_1', models.IntegerField(default=0)),
                ('gol_2', models.IntegerField(default=0)),
                ('winner', models.BooleanField(default=False)),
                ('partido_id', models.IntegerField()),
                ('wallet_id', models.IntegerField()),
            ],
        ),
    ]
