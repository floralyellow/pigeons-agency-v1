# Generated by Django 3.1.3 on 2022-10-15 16:48

import pigeon_app.models.player
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='protected_until',
            field=models.DateTimeField(default=pigeon_app.models.player.default_protected_time),
        ),
    ]