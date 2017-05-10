# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-29 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('full', models.BooleanField(default=True)),
            ],
        ),
    ]