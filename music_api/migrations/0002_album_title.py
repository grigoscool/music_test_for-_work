# Generated by Django 4.1.7 on 2023-02-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
