# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-04 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profpic', models.ImageField(upload_to='profile/')),
                ('bio', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.Project')),
            ],
        ),
    ]