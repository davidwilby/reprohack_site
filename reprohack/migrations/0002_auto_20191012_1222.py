# Generated by Django 2.2.6 on 2019-10-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_title',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_registration_url',
            new_name='registration_url',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_submission_date',
            new_name='submission_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_host',
            new_name='submitter',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_time_end',
            new_name='time_end',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_time_start',
            new_name='time_start',
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='Event title', max_length=200),
        ),
    ]
