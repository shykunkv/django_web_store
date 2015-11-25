# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20151121_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='r_name',
        ),
    ]
