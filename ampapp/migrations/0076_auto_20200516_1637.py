# Generated by Django 3.0.4 on 2020-05-16 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0075_auto_20200516_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scienceq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='studyq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
