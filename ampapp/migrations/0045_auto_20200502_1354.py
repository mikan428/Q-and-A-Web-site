# Generated by Django 3.0.4 on 2020-05-02 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0044_ine_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ine',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer'),
        ),
    ]
