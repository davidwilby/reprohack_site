# Generated by Django 3.1.4 on 2021-04-27 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack_hub', '0003_remove_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='authors_and_submitters',
        ),
    ]
