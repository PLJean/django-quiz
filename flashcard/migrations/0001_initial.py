# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-20 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=256)),
                ('back', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.ManyToManyField(to='flashcard.Category')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard.Set'),
        ),
    ]