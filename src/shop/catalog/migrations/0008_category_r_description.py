# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_product_r_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='r_description',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
