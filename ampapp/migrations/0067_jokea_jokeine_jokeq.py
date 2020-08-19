# Generated by Django 3.0.4 on 2020-05-13 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0066_hobbya_hobbyine_hobbyq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jokeine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kid', models.IntegerField(blank=True, default=0, null=True)),
                ('kidoku', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Jokeine',
            },
        ),
        migrations.CreateModel(
            name='Jokeq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Jokeq',
            },
        ),
        migrations.CreateModel(
            name='Jokea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('best', models.IntegerField(blank=True, default=0, null=True)),
                ('ip_address', models.CharField(max_length=20, verbose_name='IPアドレス')),
                ('jokeq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ampapp.Jokeq')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Jokea',
            },
        ),
    ]