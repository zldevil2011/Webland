# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181008_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='abnormalevent',
            name='device_id',
            field=models.ForeignKey(related_name='abnormalEvent', to='app.Device', null=True),
        ),
        migrations.AddField(
            model_name='abnormalevent',
            name='project_id',
            field=models.ForeignKey(related_name='abnormalEvent', to='app.Project', null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='device_id',
            field=models.ForeignKey(related_name='data', to='app.Device', null=True),
        ),
        migrations.AlterField(
            model_name='abnormalevent',
            name='event_type',
            field=models.ForeignKey(related_name='abnormalEvent', to='app.AbnormalEventType', null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(related_name='device', to='app.DeviceType', null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='owner_id',
            field=models.ForeignKey(related_name='device', to='app.User', null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='project_id',
            field=models.ForeignKey(related_name='device', to='app.Project', null=True),
        ),
    ]
