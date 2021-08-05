# Generated by Django 3.1.4 on 2021-07-19 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack_hub', '0007_review_public_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperreviewer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='reproducibility_description',
            field=markdownx.models.MarkdownxField(verbose_name='Briefly describe the procedure followed/tools used to reproduce it.'),
        ),
    ]
