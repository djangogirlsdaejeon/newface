# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20170701_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drama',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='dramaepisode',
            old_name='drama_id',
            new_name='drama',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='drama_id',
            new_name='drama',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='episode_id',
            new_name='episode',
        ),
        migrations.RenameField(
            model_name='itemcomment',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='itemfeedback',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='itemphoto',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='itemreview',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='drama_id',
            new_name='drama',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='episode_id',
            new_name='episode',
        ),
    ]
