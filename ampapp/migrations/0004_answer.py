# Generated by Django 3.0.4 on 2020-04-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0003_auto_20200409_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
            ],
            options={
                'verbose_name_plural': 'Answer',
            },
        ),
    ]
