# Generated by Django 3.0.4 on 2020-05-09 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0054_gamea_gameine_gameq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamea',
            name='diary',
        ),
        migrations.AddField(
            model_name='gamea',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ampapp.GameQ'),
        ),
    ]
