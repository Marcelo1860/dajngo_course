# Generated by Django 4.1.4 on 2022-12-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_creado_post_modificado_post_publicado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('recluter', 'Recluter'), ('publicado', 'Publicado')], default='recluter', max_length=10),
        ),
    ]
