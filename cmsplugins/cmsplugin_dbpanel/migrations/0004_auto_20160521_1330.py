# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_dbpanel', '0003_dashboardpanelmodel_refresh_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardpanelmodel',
            name='refresh_interval',
            field=models.PositiveSmallIntegerField(default=5000, verbose_name='refresh interval'),
        ),
    ]
