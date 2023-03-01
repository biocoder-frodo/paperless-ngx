# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0014_document_checksum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="checksum",
            field=models.CharField(
                editable=False,
                help_text="The checksum of the original document (before it was encrypted).  We use this to prevent duplicate document imports.",
                max_length=32,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="correspondent",
            name="is_insensitive",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="is_insensitive",
            field=models.BooleanField(default=True),
        ),
    ]