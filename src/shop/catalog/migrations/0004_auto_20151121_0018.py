# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rname',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to=b'images/products/main'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_caption',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rdescription',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rname',
            field=models.CharField(default='null', unique=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='null', upload_to=b'images/products/thumbnails'),
            preserve_default=False,
        ),
    ]
