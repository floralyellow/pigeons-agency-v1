# Generated by Django 3.1.3 on 2022-10-03 15:50

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(default=0)),
                ('encounter', models.IntegerField(default=0)),
                ('nb_tries', models.IntegerField(default=0)),
                ('is_success', models.BooleanField(default=False)),
                ('reward_droppings', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('completed_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atk_tot_score', models.IntegerField(default=0)),
                ('atk_tot_phys', models.IntegerField(default=0)),
                ('atk_tot_magic', models.IntegerField(default=0)),
                ('atk_shield_value', models.IntegerField(default=0)),
                ('atk_shield_blocs', models.IntegerField(default=0)),
                ('def_tot_score', models.IntegerField(default=0)),
                ('def_tot_phys', models.IntegerField(default=0)),
                ('def_tot_magic', models.IntegerField(default=0)),
                ('def_shield_value', models.IntegerField(default=0)),
                ('def_shield_blocs', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('winner_id', models.IntegerField(default=0)),
                ('stolen_droppings', models.IntegerField(default=0)),
                ('atk_old_military_score', models.IntegerField(default=0)),
                ('atk_new_military_score', models.IntegerField(default=0)),
                ('def_old_military_score', models.IntegerField(default=0)),
                ('def_new_military_score', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PvePigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pigeon_type', models.IntegerField(default=1)),
                ('name', models.CharField(default='test', max_length=30)),
                ('src', models.CharField(default='test', max_length=30)),
                ('pigeon_id', models.IntegerField(default=1)),
                ('lvl', models.IntegerField(default=1)),
                ('luck', models.IntegerField(default=1)),
                ('phys_atk', models.IntegerField(default=1)),
                ('magic_atk', models.IntegerField(default=1)),
                ('shield', models.IntegerField(default=0)),
                ('droppings_minute', models.IntegerField(default=1)),
                ('feathers', models.IntegerField(default=1)),
                ('creation_time', models.DateTimeField(null=True)),
                ('active_time', models.DateTimeField(null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_in_team_A', models.BooleanField(default=False)),
                ('is_in_team_B', models.BooleanField(default=False)),
                ('player_id', models.IntegerField(default=-1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TR_Expedition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(db_index=True, default=1)),
                ('seeds', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('name', models.CharField(default='test', max_length=30)),
                ('min_drop_minute', models.IntegerField(default=0)),
                ('max_drop_minute', models.IntegerField(default=0)),
                ('min_feathers', models.IntegerField(default=0)),
                ('max_feathers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TR_Lvl_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(db_index=True, default=1)),
                ('seeds_minute', models.IntegerField(default=0)),
                ('max_seeds', models.IntegerField(default=0)),
                ('max_droppings', models.IntegerField(default=0)),
                ('max_feathers', models.IntegerField(default=0)),
                ('max_pigeons', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='TR_Pigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl_expedition', models.IntegerField(db_index=True, default=1)),
                ('pigeon_type', models.IntegerField(default=1)),
                ('pigeon_id', models.IntegerField(default=1)),
                ('name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None)),
                ('src', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None)),
                ('min_phys_atk', models.IntegerField(default=1)),
                ('max_phys_atk', models.IntegerField(default=1)),
                ('min_magic_atk', models.IntegerField(default=1)),
                ('max_magic_atk', models.IntegerField(default=1)),
                ('min_shield', models.IntegerField(default=1)),
                ('max_shield', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(default=1)),
                ('seeds', models.IntegerField(default=15)),
                ('droppings', models.IntegerField(default=0)),
                ('feathers', models.IntegerField(default=0)),
                ('military_score', models.IntegerField(default=0)),
                ('last_attacked', models.IntegerField(default=-1)),
                ('time_last_attack', models.DateTimeField(auto_now_add=True, null=True)),
                ('defense_team', models.CharField(default='A', max_length=1)),
                ('last_connected_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pigeon_type', models.IntegerField(default=1)),
                ('name', models.CharField(default='test', max_length=30)),
                ('src', models.CharField(default='test', max_length=30)),
                ('pigeon_id', models.IntegerField(default=1)),
                ('lvl', models.IntegerField(default=1)),
                ('luck', models.IntegerField(default=1)),
                ('phys_atk', models.IntegerField(default=1)),
                ('magic_atk', models.IntegerField(default=1)),
                ('shield', models.IntegerField(default=0)),
                ('droppings_minute', models.IntegerField(default=1)),
                ('feathers', models.IntegerField(default=1)),
                ('creation_time', models.DateTimeField(null=True)),
                ('active_time', models.DateTimeField(null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_in_team_A', models.BooleanField(default=False)),
                ('is_in_team_B', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pigeon_app.player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttackPigeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attacker', models.BooleanField(default=False)),
                ('phys_atk_bonus', models.IntegerField(default=0)),
                ('magic_atk_bonus', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('attack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pigeon_app.attack')),
                ('pigeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pigeon_app.pigeon')),
            ],
        ),
        migrations.AddField(
            model_name='attack',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_player_atk', to='pigeon_app.player'),
        ),
        migrations.AddField(
            model_name='attack',
            name='defender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_def', to='pigeon_app.player'),
        ),
        migrations.CreateModel(
            name='AdventureAttack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atk_tot_score', models.IntegerField(default=0)),
                ('atk_tot_phys', models.IntegerField(default=0)),
                ('atk_tot_magic', models.IntegerField(default=0)),
                ('atk_shield_value', models.IntegerField(default=0)),
                ('atk_shield_blocs', models.IntegerField(default=0)),
                ('def_tot_score', models.IntegerField(default=0)),
                ('def_tot_phys', models.IntegerField(default=0)),
                ('def_tot_magic', models.IntegerField(default=0)),
                ('def_shield_value', models.IntegerField(default=0)),
                ('def_shield_blocs', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_victory', models.BooleanField(default=False)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_adventure', to='pigeon_app.adventure')),
                ('attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adventureattack_player_atk', to='pigeon_app.player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='adventure',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pigeon_app.player'),
        ),
    ]
