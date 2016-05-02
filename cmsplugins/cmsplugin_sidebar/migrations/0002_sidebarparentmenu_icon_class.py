# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_sidebar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebarparentmenu',
            name='icon_class',
            field=models.CharField(default=b'fa fa-bar-chart-o fa-fw', max_length=40),
        ),
    ]
