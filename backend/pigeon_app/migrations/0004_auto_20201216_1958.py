# Generated by Django 3.1.3 on 2020-12-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon_app', '0003_tr_expedition_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeon',
            name='active_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pigeon',
            name='creation_time',
            field=models.DateTimeField(null=True),
        ),
    ]