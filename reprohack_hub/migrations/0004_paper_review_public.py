# Generated by Django 3.1.4 on 2021-06-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack_hub', '0003_auto_20210603_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='review_public',
            field=models.BooleanField(default=True, verbose_name='Make reviews public'),
        ),
    ]
