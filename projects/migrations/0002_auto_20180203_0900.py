# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-03 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='division',
            field=models.CharField(choices=[('Pumps', 'Pumps'), ('Pipes', 'Pipes'), ('Power Banks', 'Power Banks')], default='Pumps', max_length=25),
        ),
        migrations.DeleteModel(
            name='Division',
        ),
    ]
