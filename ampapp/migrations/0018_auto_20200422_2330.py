# Generated by Django 3.0.4 on 2020-04-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0017_auto_20200422_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='read',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='readtext',
        ),
        migrations.CreateModel(
            name='Ine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20, verbose_name='IPアドレス')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer')),
            ],
            options={
                'verbose_name_plural': 'Ine',
            },
        ),
    ]
