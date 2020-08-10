# Generated by Django 3.0.7 on 2020-08-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0006_auto_20200809_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='advantages',
            field=models.TextField(verbose_name='What were the positive features of this approach?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='challenges',
            field=models.TextField(verbose_name='What were the main challenges you ran into (if any)?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments_and_suggestions',
            field=models.TextField(verbose_name='Any other comments/suggestions on the reproducibility approach?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='documentation_cons',
            field=models.TextField(verbose_name='How could the documentation be improved?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='documentation_pros',
            field=models.TextField(verbose_name='What do you like about the documentation?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='familiarity_with_method',
            field=models.TextField(verbose_name='Briefly describe your familiarity with the procedure/tools used by the paper.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reproducibility_description',
            field=models.TextField(verbose_name='Briefly describe the procedure followed/toolsused to reproduce it.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='software_installed',
            field=models.TextField(verbose_name='What additional software did you need to install?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='software_used',
            field=models.TextField(verbose_name='What software did you use?'),
        ),
        migrations.AlterField(
            model_name='review',
            name='transparency_suggestions',
            field=models.TextField(verbose_name='Any suggestions on how the analysis could be made more transparent?'),
        ),
    ]