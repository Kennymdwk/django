# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-15 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160715_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=250, verbose_name='Название склада')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=250, verbose_name='Название организации')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='consumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Consumer', verbose_name='кому'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Supplier', verbose_name='от кого'),
        ),
    ]
