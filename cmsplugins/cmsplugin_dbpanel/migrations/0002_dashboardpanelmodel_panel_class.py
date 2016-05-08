# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_dbpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpanelmodel',
            name='panel_class',
            field=models.CharField(default=b'default', max_length=10, verbose_name='panel class', choices=[(b'default', 'default'), (b'primary', 'primary'), (b'success', 'success'), (b'info', 'info'), (b'warning', 'warning'), (b'danger', 'danger'), (b'green', 'green'), (b'yellow', 'yellow'), (b'red', 'red')]),
        ),
    ]
