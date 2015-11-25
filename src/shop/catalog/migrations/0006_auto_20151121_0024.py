# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20151121_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='rname',
            new_name='r_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rdescription',
            new_name='r_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rname',
            new_name='r_name',
        ),
    ]
