## -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-19 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160715_1552'),
        ('oil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
