# Generated by Django 2.1.2 on 2019-10-08 04:10

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_provider', '0022_auto_20190918_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='ip_used',
            field=common.models.JsonListTextField(default=[], null=True),
        ),
    ]
