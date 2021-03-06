# Generated by Django 3.0.4 on 2020-04-23 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0018_auto_20200422_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='ine',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ine',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ine',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer'),
        ),
    ]
