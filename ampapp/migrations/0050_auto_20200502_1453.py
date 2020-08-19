# Generated by Django 3.0.4 on 2020-05-02 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0049_auto_20200502_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='ine',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ampapp.Answer'),
        ),
        migrations.AddField(
            model_name='ine',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
            preserve_default=False,
        ),
    ]
