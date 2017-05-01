# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 15:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_personal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='name',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='published_date',
        ),
        migrations.AddField(
            model_name='personal',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personal',
            name='cgpa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='personal',
            name='email',
            field=models.EmailField(default='sniranjanamvk@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='personal',
            name='user',
            field=models.CharField(default='meeru', max_length=30),
        ),
        migrations.AlterField(
            model_name='personal',
            name='rollno',
            field=models.IntegerField(default=0),
        ),
    ]
