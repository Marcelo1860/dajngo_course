# Generated by Django 4.1.4 on 2022-12-08 16:06

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 8, 16, 6, 15, 638179, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publicado', 'Publicado'), ('recluter', 'Recluter')], default='recluter', max_length=10),
        ),
    ]
