# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181008_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('img_src', models.TextField()),
                ('device_num', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='device_num',
        ),
        migrations.AddField(
            model_name='abnormalevent',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='abnormaleventtype',
            name='value',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
