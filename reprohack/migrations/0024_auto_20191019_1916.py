# Generated by Django 2.2.6 on 2019-10-19 19:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('reprohack', '0023_auto_20191017_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Event title', max_length=200)),
                ('citation_txt', models.CharField(max_length=500)),
                ('doi', models.CharField(default='10.1000/xyz123', max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('why', models.CharField(max_length=500)),
                ('focus', models.CharField(max_length=500)),
                ('paper_url', models.URLField()),
                ('code_url', models.URLField()),
                ('data_url', models.URLField()),
                ('extra_url', models.URLField()),
                ('citation_bib', models.CharField(max_length=800)),
                ('twitter', models.CharField(max_length=40)),
                ('github', models.CharField(max_length=40)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tools', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 47, 88025)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 47, 87990)),
        ),
        migrations.CreateModel(
            name='ReportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(through='reprohack.Membership', to=settings.AUTH_USER_MODEL)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reprohack.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='report_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reprohack.ReportGroup'),
        ),
    ]
