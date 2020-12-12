# Generated by Django 3.1.3 on 2020-12-12 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(default=1)),
                ('seeds', models.IntegerField(default=0)),
                ('droppings', models.IntegerField(default=0)),
                ('military_score', models.IntegerField(default=0)),
                ('last_connected_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('feathers', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_type', models.IntegerField(default=1)),
                ('name', models.CharField(default='test', max_length=30)),
                ('element', models.IntegerField(default=1)),
                ('attack', models.IntegerField(default=1)),
                ('defense', models.IntegerField(default=1)),
                ('shield', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=1)),
                ('droppings_minute', models.IntegerField(default=1)),
                ('feathers', models.IntegerField(default=1)),
                ('creation_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('active_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_attacker', models.BooleanField(default=False)),
                ('is_defender', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pigeon_app.player')),
            ],
        ),
    ]
