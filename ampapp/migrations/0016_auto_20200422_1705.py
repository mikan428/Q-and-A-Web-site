# Generated by Django 3.0.4 on 2020-04-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0015_diary_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='read',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='readtext',
        ),
        migrations.AddField(
            model_name='answer',
            name='read',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='readtext',
            field=models.CharField(max_length=40, null=True, verbose_name='いいね'),
        ),
    ]
