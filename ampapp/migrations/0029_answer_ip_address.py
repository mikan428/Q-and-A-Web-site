# Generated by Django 3.0.4 on 2020-04-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0028_answer_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='ip_address',
            field=models.CharField(default=1, max_length=20, verbose_name='IPアドレス'),
            preserve_default=False,
        ),
    ]
