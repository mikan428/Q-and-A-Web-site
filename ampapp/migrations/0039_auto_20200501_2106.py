# Generated by Django 3.0.4 on 2020-05-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0038_auto_20200501_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='readtext',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]