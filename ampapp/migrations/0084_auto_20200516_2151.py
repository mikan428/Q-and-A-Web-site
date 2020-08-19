# Generated by Django 3.0.4 on 2020-05-16 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0083_auto_20200516_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencea',
            name='name',
            field=models.CharField(default=1, max_length=40, verbose_name='名前'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scienceq',
            name='ip_address',
            field=models.CharField(default=1, max_length=20, verbose_name='IPアドレス'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scienceq',
            name='name',
            field=models.CharField(default=1, max_length=40, verbose_name='名前'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sciencea',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='scienceq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
