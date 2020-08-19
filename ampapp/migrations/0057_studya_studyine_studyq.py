# Generated by Django 3.0.4 on 2020-05-10 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ampapp', '0056_auto_20200509_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studyine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kid', models.IntegerField(blank=True, default=0, null=True)),
                ('kidoku', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gameine',
            },
        ),
        migrations.CreateModel(
            name='Studyq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('views', models.PositiveIntegerField(default=0)),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('goodtext', models.CharField(blank=True, default='a', max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'GameQ',
            },
        ),
        migrations.CreateModel(
            name='Studya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readtext', models.CharField(blank=True, default='a', max_length=100, null=True)),
                ('best', models.IntegerField(blank=True, default=0, null=True)),
                ('ip_address', models.CharField(max_length=20, verbose_name='IPアドレス')),
                ('studyq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ampapp.Studyq')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'GameA',
            },
        ),
    ]
