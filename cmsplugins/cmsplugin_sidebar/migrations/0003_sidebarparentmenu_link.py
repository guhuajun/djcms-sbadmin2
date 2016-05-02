# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_sidebar', '0002_sidebarparentmenu_icon_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebarparentmenu',
            name='link',
            field=models.CharField(default=b'#', max_length=200),
        ),
    ]
