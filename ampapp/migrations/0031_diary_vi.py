# Generated by Django 3.0.4 on 2020-04-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0030_answer_readtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='vi',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
