# Generated by Django 3.0.4 on 2020-05-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0086_auto_20200516_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentq',
            name='ip_address',
            field=models.CharField(default=1, max_length=20, verbose_name='IPアドレス'),
            preserve_default=False,
        ),
    ]
