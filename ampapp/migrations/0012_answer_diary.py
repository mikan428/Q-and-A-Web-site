# Generated by Django 3.0.4 on 2020-04-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampapp', '0011_remove_answer_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='diary',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ampapp.Diary'),
            preserve_default=False,
        ),
    ]
