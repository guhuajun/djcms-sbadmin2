# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardPanelModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('description', models.CharField(max_length=20, verbose_name='description')),
                ('icon_class', models.CharField(default=b'fa fa-bar-chart-o fa-fw', max_length=40, verbose_name='icon class')),
                ('data_source', models.URLField(verbose_name='data source')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
