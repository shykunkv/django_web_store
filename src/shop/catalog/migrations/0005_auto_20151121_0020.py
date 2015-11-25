# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20151121_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rname',
            field=models.CharField(max_length=255),
        ),
    ]
