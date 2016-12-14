# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cover', models.ImageField(upload_to='covers/%Y/%m/%d/', verbose_name='cover')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='caption')),
            ],
            options={
                'verbose_name_plural': 'Covers',
                'verbose_name': 'Cover',
            },
        ),
    ]