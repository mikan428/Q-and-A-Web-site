# Generated by Django 3.0.4 on 2020-05-16 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0080_auto_20200516_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamea',
            name='name',
            field=models.CharField(default=1, max_length=40, verbose_name='名前'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamea',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='gameq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]