# Generated by Django 3.0.4 on 2020-05-02 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0046_auto_20200502_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ine',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer'),
        ),
    ]
