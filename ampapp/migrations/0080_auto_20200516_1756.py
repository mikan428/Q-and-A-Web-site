# Generated by Django 3.0.4 on 2020-05-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0079_auto_20200516_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(null=True, verbose_name='本文'),
        ),
    ]
