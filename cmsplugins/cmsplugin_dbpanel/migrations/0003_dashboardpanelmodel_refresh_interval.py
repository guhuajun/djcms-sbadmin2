# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_dbpanel', '0002_dashboardpanelmodel_panel_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpanelmodel',
            name='refresh_interval',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='refresh interval'),
        ),
    ]
