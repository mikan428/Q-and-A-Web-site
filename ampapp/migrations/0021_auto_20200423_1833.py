# Generated by Django 3.0.4 on 2020-04-23 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0020_auto_20200423_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ine',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer'),
        ),
    ]
