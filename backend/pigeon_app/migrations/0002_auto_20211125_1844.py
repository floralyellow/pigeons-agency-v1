# Generated by Django 3.1.3 on 2021-11-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='seeds',
            field=models.IntegerField(default=15),
        ),
    ]
