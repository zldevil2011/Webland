# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181009_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='airData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('windySpeed', models.FloatField(null=True)),
                ('windyDirection', models.IntegerField(null=True)),
                ('pm25', models.FloatField(null=True)),
                ('pm10', models.FloatField(null=True)),
                ('o3', models.FloatField(null=True)),
                ('co', models.FloatField(null=True)),
                ('so2', models.FloatField(null=True)),
                ('no2', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='meteorologyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('windySpeed', models.FloatField(null=True)),
                ('windyDirection', models.IntegerField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('noise', models.FloatField(null=True)),
                ('pressure', models.FloatField(null=True)),
                ('light', models.FloatField(null=True)),
                ('rainy', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='soilData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('conductivity', models.FloatField(null=True)),
                ('ph', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='waterData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('waterLevel', models.FloatField(null=True)),
                ('o3', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('elec', models.FloatField(null=True)),
                ('conductivity', models.FloatField(null=True)),
                ('ph', models.FloatField(null=True)),
                ('transparency', models.FloatField(null=True)),
                ('waterSpeed', models.FloatField(null=True)),
                ('nh4', models.FloatField(null=True)),
            ],
        ),
    ]
