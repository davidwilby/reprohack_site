# Generated by Django 2.2.6 on 2019-10-16 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0018_auto_20191016_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 49, 803571)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 49, 803538)),
        ),
    ]
