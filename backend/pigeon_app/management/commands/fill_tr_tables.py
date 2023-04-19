from django.core.management.base import BaseCommand

from ...models import TR_Expedition, TR_Lvl_info, TR_Pigeon


class Command(BaseCommand):
    help = 'Fills tr tables'

    def add_arguments(self, parser):
        # Positional arguments
       parser.add_argument('--force_recreate', type=str)

    def handle(self, *args, **kwargs):

        if TR_Lvl_info.objects.count() == 0 or kwargs['force_recreate'] == 'TRUE':
            
            TR_Lvl_info.objects.all().delete() 
            TR_Lvl_info.objects.bulk_create([

            TR_Lvl_info(lvl=1,seeds_minute=75,max_seeds=27,max_droppings=90,max_feathers=15,max_pigeons=10),
            TR_Lvl_info(lvl=2,seeds_minute=100,max_seeds=55,max_droppings=270,max_feathers=60,max_pigeons=12),
            TR_Lvl_info(lvl=3,seeds_minute=150,max_seeds=110,max_droppings=740,max_feathers=240,max_pigeons=14),
            TR_Lvl_info(lvl=4,seeds_minute=250,max_seeds=220,max_droppings=1080,max_feathers=720,max_pigeons=16),
            TR_Lvl_info(lvl=5,seeds_minute=350,max_seeds=420,max_droppings=2070,max_feathers=1584,max_pigeons=18),
            TR_Lvl_info(lvl=6,seeds_minute=450,max_seeds=1000,max_droppings=4800,max_feathers=3132,max_pigeons=20),
            TR_Lvl_info(lvl=7,seeds_minute=550,max_seeds=1700,max_droppings=8800,max_feathers=6045,max_pigeons=22),
            TR_Lvl_info(lvl=8,seeds_minute=650,max_seeds=2650,max_droppings=17160,max_feathers=11550,max_pigeons=24),
            TR_Lvl_info(lvl=9,seeds_minute=750,max_seeds=4200,max_droppings=31690,max_feathers=21375,max_pigeons=26),
            TR_Lvl_info(lvl=10,seeds_minute=850,max_seeds=6100,max_droppings=52540,max_feathers=36000,max_pigeons=28),
            TR_Lvl_info(lvl=11,seeds_minute=950,max_seeds=8400,max_droppings=79350,max_feathers=56100,max_pigeons=30),
            TR_Lvl_info(lvl=12,seeds_minute=1050,max_seeds=13400,max_droppings=115560,max_feathers=83700,max_pigeons=32),
            TR_Lvl_info(lvl=13,seeds_minute=1150,max_seeds=16500,max_droppings=155550,max_feathers=119700,max_pigeons=34),
            TR_Lvl_info(lvl=14,seeds_minute=1250,max_seeds=20000,max_droppings=211140,max_feathers=168000,max_pigeons=36),
            TR_Lvl_info(lvl=15,seeds_minute=1350,max_seeds=23600,max_droppings=291750,max_feathers=233100,max_pigeons=38),
            TR_Lvl_info(lvl=16,seeds_minute=1450,max_seeds=28200,max_droppings=393600,max_feathers=320100,max_pigeons=40),
            TR_Lvl_info(lvl=17,seeds_minute=1550,max_seeds=33000,max_droppings=515030,max_feathers=431250,max_pigeons=42),
            TR_Lvl_info(lvl=18,seeds_minute=1650,max_seeds=38000,max_droppings=646800,max_feathers=576000,max_pigeons=44),
            TR_Lvl_info(lvl=19,seeds_minute=1750,max_seeds=42800,max_droppings=794710,max_feathers=787500,max_pigeons=46),
            TR_Lvl_info(lvl=20,seeds_minute=1850,max_seeds=48000,max_droppings=1014120,max_feathers=1053000,max_pigeons=48),
            TR_Lvl_info(lvl=21,seeds_minute=1950,max_seeds=68000,max_droppings=1364000,max_feathers=1336500,max_pigeons=50),
            TR_Lvl_info(lvl=22,seeds_minute=2050,max_seeds=80000,max_droppings=1723800,max_feathers=1638000,max_pigeons=52),
            TR_Lvl_info(lvl=23,seeds_minute=2150,max_seeds=91500,max_droppings=2142860,max_feathers=1957500,max_pigeons=54),
            TR_Lvl_info(lvl=24,seeds_minute=2250,max_seeds=103000,max_droppings=2620800,max_feathers=2295000,max_pigeons=56),
            TR_Lvl_info(lvl=25,seeds_minute=2350,max_seeds=115000,max_droppings=3118230,max_feathers=2650500,max_pigeons=58),
            TR_Lvl_info(lvl=26,seeds_minute=2450,max_seeds=138000,max_droppings=4005750,max_feathers=3312000,max_pigeons=60),
            TR_Lvl_info(lvl=27,seeds_minute=2550,max_seeds=162000,max_droppings=4978600,max_feathers=4009500,max_pigeons=62),
            TR_Lvl_info(lvl=28,seeds_minute=2650,max_seeds=186000,max_droppings=6030640,max_feathers=4794000,max_pigeons=64),
            TR_Lvl_info(lvl=29,seeds_minute=2750,max_seeds=210000,max_droppings=7143760,max_feathers=5775000,max_pigeons=66),
            TR_Lvl_info(lvl=30,seeds_minute=2850,max_seeds=230000,max_droppings=8675100,max_feathers=7020000,max_pigeons=68),

            ])

        if TR_Pigeon.objects.count() == 0 or kwargs['force_recreate'] == 'TRUE':

            TR_Pigeon.objects.all().delete() 
            TR_Pigeon.objects.bulk_create([

            TR_Pigeon(lvl_expedition=1,pigeon_type=1,pigeon_id=1,src=["pidgetassium_yellow.png"],name=["Pidgetassium"],min_phys_atk=10,max_phys_atk=20,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=2,pigeon_type=1,pigeon_id=2,src=["cactigeon_green.png"],name=["Cactigeon"],min_phys_atk=17,max_phys_atk=28,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=3,pigeon_type=1,pigeon_id=3,src=["bombird_black.png"],name=["Bombird"],min_phys_atk=24,max_phys_atk=36,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=4,pigeon_type=1,pigeon_id=4,src=["ninjeon_black.png"],name=["Ninjeon"],min_phys_atk=31,max_phys_atk=45,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=5,pigeon_type=1,pigeon_id=5,src=["pidgetassium_brown.png"],name=["Pidgetassium"],min_phys_atk=38,max_phys_atk=54,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=6,pigeon_type=1,pigeon_id=6,src=["cactigeon_red.png"],name=["Cactigeon"],min_phys_atk=46,max_phys_atk=64,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=7,pigeon_type=1,pigeon_id=7,src=["bombird_green.png"],name=["Bombird"],min_phys_atk=55,max_phys_atk=76,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=8,pigeon_type=1,pigeon_id=8,src=["ninjeon_grey.png"],name=["Ninjeon"],min_phys_atk=66,max_phys_atk=90,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=9,pigeon_type=1,pigeon_id=9,src=["pidgetassium_green.png"],name=["Pidgetassium"],min_phys_atk=79,max_phys_atk=106,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=10,pigeon_type=1,pigeon_id=10,src=["cactigeon_yellow.png"],name=["Cactigeon"],min_phys_atk=94,max_phys_atk=124,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=11,pigeon_type=1,pigeon_id=11,src=["bombird_red.png"],name=["Bombird"],min_phys_atk=110,max_phys_atk=143,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=12,pigeon_type=1,pigeon_id=12,src=["ninjeon_white.png"],name=["Ninjeon"],min_phys_atk=128,max_phys_atk=164,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=13,pigeon_type=1,pigeon_id=13,src=["pidgetassium_yellow.png"],name=["Pidgetassium"],min_phys_atk=147,max_phys_atk=187,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=14,pigeon_type=1,pigeon_id=14,src=["cactigeon_green.png"],name=["Cactigeon"],min_phys_atk=169,max_phys_atk=213,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=15,pigeon_type=1,pigeon_id=15,src=["bombird_black.png"],name=["Bombird"],min_phys_atk=193,max_phys_atk=241,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=16,pigeon_type=1,pigeon_id=16,src=["ninjeon_black.png"],name=["Ninjeon"],min_phys_atk=220,max_phys_atk=272,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=17,pigeon_type=1,pigeon_id=17,src=["pidgetassium_brown.png"],name=["Pidgetassium"],min_phys_atk=249,max_phys_atk=305,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=18,pigeon_type=1,pigeon_id=18,src=["cactigeon_red.png"],name=["Cactigeon"],min_phys_atk=280,max_phys_atk=340,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=19,pigeon_type=1,pigeon_id=19,src=["bombird_green.png"],name=["Bombird"],min_phys_atk=314,max_phys_atk=378,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=20,pigeon_type=1,pigeon_id=20,src=["ninjeon_grey.png"],name=["Ninjeon"],min_phys_atk=351,max_phys_atk=419,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=21,pigeon_type=1,pigeon_id=21,src=["pidgetassium_green.png"],name=["Pidgetassium"],min_phys_atk=391,max_phys_atk=463,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=22,pigeon_type=1,pigeon_id=22,src=["cactigeon_yellow.png"],name=["Cactigeon"],min_phys_atk=435,max_phys_atk=511,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=23,pigeon_type=1,pigeon_id=23,src=["bombird_red.png"],name=["Bombird"],min_phys_atk=483,max_phys_atk=563,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=24,pigeon_type=1,pigeon_id=24,src=["ninjeon_white.png"],name=["Ninjeon"],min_phys_atk=537,max_phys_atk=621,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=25,pigeon_type=1,pigeon_id=25,src=["pidgetassium_yellow.png"],name=["Pidgetassium"],min_phys_atk=595,max_phys_atk=683,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=26,pigeon_type=1,pigeon_id=26,src=["cactigeon_green.png"],name=["Cactigeon"],min_phys_atk=656,max_phys_atk=748,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=27,pigeon_type=1,pigeon_id=27,src=["bombird_black.png"],name=["Bombird"],min_phys_atk=721,max_phys_atk=817,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=28,pigeon_type=1,pigeon_id=28,src=["cactigeon_yellow.png"],name=["Cactigeon"],min_phys_atk=791,max_phys_atk=891,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=29,pigeon_type=1,pigeon_id=29,src=["pidgetassium_brown.png"],name=["Pidgetassium"],min_phys_atk=866,max_phys_atk=971,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=30,pigeon_type=1,pigeon_id=30,src=["ninjeon_black.png"],name=["Ninjeon"],min_phys_atk=948,max_phys_atk=1058,min_magic_atk=0,max_magic_atk=0,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=1,pigeon_type=3,pigeon_id=31,src=["eggeon_beige.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=5,max_magic_atk=10,min_shield=2,max_shield=3),
            TR_Pigeon(lvl_expedition=2,pigeon_type=3,pigeon_id=32,src=["watermegeon_green.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=9,max_magic_atk=14,min_shield=3,max_shield=4),
            TR_Pigeon(lvl_expedition=3,pigeon_type=3,pigeon_id=33,src=["stone_rubygeon.png"],name=["Rubygeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=12,max_magic_atk=18,min_shield=4,max_shield=5),
            TR_Pigeon(lvl_expedition=4,pigeon_type=3,pigeon_id=34,src=["eggeon_white.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=16,max_magic_atk=22,min_shield=5,max_shield=6),
            TR_Pigeon(lvl_expedition=5,pigeon_type=3,pigeon_id=35,src=["watermegeon_brown.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=19,max_magic_atk=27,min_shield=6,max_shield=8),
            TR_Pigeon(lvl_expedition=6,pigeon_type=3,pigeon_id=36,src=["stone_saphirgeon.png"],name=["Saphirgeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=23,max_magic_atk=32,min_shield=7,max_shield=9),
            TR_Pigeon(lvl_expedition=7,pigeon_type=3,pigeon_id=37,src=["eggeon_blue.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=28,max_magic_atk=38,min_shield=8,max_shield=11),
            TR_Pigeon(lvl_expedition=8,pigeon_type=3,pigeon_id=38,src=["watermegeon_blue.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=33,max_magic_atk=45,min_shield=10,max_shield=13),
            TR_Pigeon(lvl_expedition=9,pigeon_type=3,pigeon_id=39,src=["stone_glassgeon.png"],name=["Glassgeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=40,max_magic_atk=53,min_shield=12,max_shield=15),
            TR_Pigeon(lvl_expedition=10,pigeon_type=3,pigeon_id=40,src=["eggeon_beige.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=47,max_magic_atk=62,min_shield=14,max_shield=18),
            TR_Pigeon(lvl_expedition=11,pigeon_type=3,pigeon_id=41,src=["watermegeon_red.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=55,max_magic_atk=71,min_shield=17,max_shield=21),
            TR_Pigeon(lvl_expedition=12,pigeon_type=3,pigeon_id=42,src=["stone_emergeon.png"],name=["Emergeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=64,max_magic_atk=82,min_shield=19,max_shield=24),
            TR_Pigeon(lvl_expedition=13,pigeon_type=3,pigeon_id=43,src=["eggeon_beige.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=74,max_magic_atk=93,min_shield=22,max_shield=28),
            TR_Pigeon(lvl_expedition=14,pigeon_type=3,pigeon_id=44,src=["watermegeon_green.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=85,max_magic_atk=106,min_shield=25,max_shield=31),
            TR_Pigeon(lvl_expedition=15,pigeon_type=3,pigeon_id=45,src=["stone_diamgeon.png"],name=["Diamgeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=97,max_magic_atk=120,min_shield=29,max_shield=36),
            TR_Pigeon(lvl_expedition=16,pigeon_type=3,pigeon_id=46,src=["eggeon_white.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=110,max_magic_atk=136,min_shield=33,max_shield=40),
            TR_Pigeon(lvl_expedition=17,pigeon_type=3,pigeon_id=47,src=["watermegeon_brown.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=125,max_magic_atk=152,min_shield=37,max_shield=45),
            TR_Pigeon(lvl_expedition=18,pigeon_type=3,pigeon_id=48,src=["stone_saphirgeon.png"],name=["Saphirgeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=140,max_magic_atk=170,min_shield=42,max_shield=51),
            TR_Pigeon(lvl_expedition=19,pigeon_type=3,pigeon_id=49,src=["eggeon_blue.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=157,max_magic_atk=189,min_shield=47,max_shield=56),
            TR_Pigeon(lvl_expedition=20,pigeon_type=3,pigeon_id=50,src=["watermegeon_blue.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=176,max_magic_atk=209,min_shield=53,max_shield=62),
            TR_Pigeon(lvl_expedition=21,pigeon_type=3,pigeon_id=51,src=["stone_rubygeon.png"],name=["Rubygeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=196,max_magic_atk=231,min_shield=59,max_shield=69),
            TR_Pigeon(lvl_expedition=22,pigeon_type=3,pigeon_id=52,src=["eggeon_beige.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=218,max_magic_atk=255,min_shield=65,max_shield=76),
            TR_Pigeon(lvl_expedition=23,pigeon_type=3,pigeon_id=53,src=["watermegeon_red.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=242,max_magic_atk=281,min_shield=72,max_shield=84),
            TR_Pigeon(lvl_expedition=24,pigeon_type=3,pigeon_id=54,src=["stone_emergeon.png"],name=["Emergeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=269,max_magic_atk=310,min_shield=81,max_shield=93),
            TR_Pigeon(lvl_expedition=25,pigeon_type=3,pigeon_id=55,src=["eggeon_beige.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=298,max_magic_atk=341,min_shield=89,max_shield=102),
            TR_Pigeon(lvl_expedition=26,pigeon_type=3,pigeon_id=56,src=["watermegeon_green.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=328,max_magic_atk=374,min_shield=98,max_shield=112),
            TR_Pigeon(lvl_expedition=27,pigeon_type=3,pigeon_id=57,src=["stone_emergeon.png"],name=["Emergeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=361,max_magic_atk=408,min_shield=108,max_shield=122),
            TR_Pigeon(lvl_expedition=28,pigeon_type=3,pigeon_id=58,src=["eggeon_white.png"],name=["Eggeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=396,max_magic_atk=445,min_shield=119,max_shield=133),
            TR_Pigeon(lvl_expedition=29,pigeon_type=3,pigeon_id=59,src=["watermegeon_brown.png"],name=["Watermegeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=433,max_magic_atk=485,min_shield=130,max_shield=145),
            TR_Pigeon(lvl_expedition=30,pigeon_type=3,pigeon_id=60,src=["stone_diamgeon.png"],name=["Diamgeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=474,max_magic_atk=529,min_shield=142,max_shield=158),
            TR_Pigeon(lvl_expedition=1,pigeon_type=2,pigeon_id=61,src=["waterfowl_1.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=8,max_magic_atk=15,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=2,pigeon_type=2,pigeon_id=62,src=["toxigeon_black.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=13,max_magic_atk=21,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=3,pigeon_type=2,pigeon_id=63,src=["margeon.png"],name=["Margeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=18,max_magic_atk=27,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=4,pigeon_type=2,pigeon_id=64,src=["waterfowl_2.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=23,max_magic_atk=33,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=5,pigeon_type=2,pigeon_id=65,src=["toxigeon_purple.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=29,max_magic_atk=40,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=6,pigeon_type=2,pigeon_id=66,src=["luigeon.png"],name=["Luigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=35,max_magic_atk=48,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=7,pigeon_type=2,pigeon_id=67,src=["waterfowl_3.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=41,max_magic_atk=57,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=8,pigeon_type=2,pigeon_id=68,src=["toxigeon_green.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=50,max_magic_atk=67,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=9,pigeon_type=2,pigeon_id=69,src=["wageon.png"],name=["Wageon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=59,max_magic_atk=79,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=10,pigeon_type=2,pigeon_id=70,src=["waterfowl_1.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=71,max_magic_atk=93,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=11,pigeon_type=2,pigeon_id=71,src=["toxigeon_black.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=83,max_magic_atk=107,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=12,pigeon_type=2,pigeon_id=72,src=["waluigeon.png"],name=["Waluigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=96,max_magic_atk=123,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=13,pigeon_type=2,pigeon_id=73,src=["waterfowl_2.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=110,max_magic_atk=140,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=14,pigeon_type=2,pigeon_id=74,src=["toxigeon_purple.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=127,max_magic_atk=159,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=15,pigeon_type=2,pigeon_id=75,src=["margeon.png"],name=["Margeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=145,max_magic_atk=180,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=16,pigeon_type=2,pigeon_id=76,src=["waterfowl_3.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=165,max_magic_atk=204,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=17,pigeon_type=2,pigeon_id=77,src=["toxigeon_green.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=187,max_magic_atk=228,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=18,pigeon_type=2,pigeon_id=78,src=["luigeon.png"],name=["Luigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=210,max_magic_atk=255,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=19,pigeon_type=2,pigeon_id=79,src=["waterfowl_1.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=236,max_magic_atk=283,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=20,pigeon_type=2,pigeon_id=80,src=["toxigeon_black.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=263,max_magic_atk=314,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=21,pigeon_type=2,pigeon_id=81,src=["wageon.png"],name=["Wageon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=293,max_magic_atk=347,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=22,pigeon_type=2,pigeon_id=82,src=["waterfowl_2.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=326,max_magic_atk=383,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=23,pigeon_type=2,pigeon_id=83,src=["toxigeon_purple.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=362,max_magic_atk=422,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=24,pigeon_type=2,pigeon_id=84,src=["luigeon.png"],name=["Luigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=403,max_magic_atk=465,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=25,pigeon_type=2,pigeon_id=85,src=["waterfowl_3.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=446,max_magic_atk=512,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=26,pigeon_type=2,pigeon_id=86,src=["toxigeon_green.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=492,max_magic_atk=561,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=27,pigeon_type=2,pigeon_id=87,src=["wageon.png"],name=["Wageon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=541,max_magic_atk=612,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=28,pigeon_type=2,pigeon_id=88,src=["toxigeon_black.png"],name=["Toxigeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=593,max_magic_atk=668,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=29,pigeon_type=2,pigeon_id=89,src=["margeon.png"],name=["Margeon"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=650,max_magic_atk=728,min_shield=0,max_shield=0),
            TR_Pigeon(lvl_expedition=30,pigeon_type=2,pigeon_id=90,src=["waterfowl_1.png"],name=["Waterfowl"],min_phys_atk=0,max_phys_atk=0,min_magic_atk=711,max_magic_atk=793,min_shield=0,max_shield=0),

            ])

        if TR_Expedition.objects.count() == 0 or kwargs['force_recreate'] == 'TRUE':

            TR_Expedition.objects.all().delete() 
            TR_Expedition.objects.bulk_create([

            TR_Expedition(lvl=1,seeds=10,duration=8,name="The Eiffel Tower",min_drop_minute=1,max_drop_minute=6,min_feathers=2,max_feathers=4),
            TR_Expedition(lvl=2,seeds=20,duration=12,name="Buckingham Palace",min_drop_minute=3,max_drop_minute=6,min_feathers=4,max_feathers=8),
            TR_Expedition(lvl=3,seeds=40,duration=16,name="Mount Rushmore",min_drop_minute=5,max_drop_minute=9,min_feathers=8,max_feathers=16),
            TR_Expedition(lvl=4,seeds=80,duration=19,name="Sydney Opera House",min_drop_minute=7,max_drop_minute=11,min_feathers=16,max_feathers=32),
            TR_Expedition(lvl=5,seeds=150,duration=26,name="Golden Gate Bridge",min_drop_minute=9,max_drop_minute=14,min_feathers=32,max_feathers=64),
            TR_Expedition(lvl=6,seeds=270,duration=36,name="Taj Mahal",min_drop_minute=12,max_drop_minute=20,min_feathers=64,max_feathers=110),
            TR_Expedition(lvl=7,seeds=450,duration=49,name="Mont Saint-Michel",min_drop_minute=16,max_drop_minute=24,min_feathers=110,max_feathers=200),
            TR_Expedition(lvl=8,seeds=700,duration=65,name="La Sagrada Familia",min_drop_minute=20,max_drop_minute=32,min_feathers=200,max_feathers=350),
            TR_Expedition(lvl=9,seeds=1100,duration=88,name="Machu Picchu",min_drop_minute=24,max_drop_minute=41,min_feathers=350,max_feathers=600),
            TR_Expedition(lvl=10,seeds=1600,duration=113,name="The Great Wall of China",min_drop_minute=28,max_drop_minute=51,min_feathers=600,max_feathers=900),
            TR_Expedition(lvl=11,seeds=2200,duration=139,name="The Acropolis",min_drop_minute=32,max_drop_minute=60,min_feathers=900,max_feathers=1300),
            TR_Expedition(lvl=12,seeds=2850,duration=163,name="The Brandenburg Gate",min_drop_minute=37,max_drop_minute=70,min_feathers=1300,max_feathers=1800),
            TR_Expedition(lvl=13,seeds=3500,duration=183,name="The Great Pyramid of Giza",min_drop_minute=42,max_drop_minute=80,min_feathers=1800,max_feathers=2400),
            TR_Expedition(lvl=14,seeds=4250,duration=204,name="Leaning Tower of Pisa",min_drop_minute=47,max_drop_minute=91,min_feathers=2400,max_feathers=3200),
            TR_Expedition(lvl=15,seeds=5000,duration=222,name="Victoria Falls",min_drop_minute=57,max_drop_minute=109,min_feathers=3200,max_feathers=4200),
            TR_Expedition(lvl=16,seeds=6000,duration=248,name="Blue Domes of Oia",min_drop_minute=67,max_drop_minute=125,min_feathers=4200,max_feathers=5500),
            TR_Expedition(lvl=17,seeds=7000,duration=271,name="Blue Mosque",min_drop_minute=77,max_drop_minute=141,min_feathers=5500,max_feathers=7000),
            TR_Expedition(lvl=18,seeds=8000,duration=291,name="The Colosseum",min_drop_minute=87,max_drop_minute=158,min_feathers=7000,max_feathers=9000),
            TR_Expedition(lvl=19,seeds=9000,duration=309,name="Easter Island",min_drop_minute=97,max_drop_minute=174,min_feathers=9000,max_feathers=12000),
            TR_Expedition(lvl=20,seeds=10000,duration=324,name="Angkor Wat",min_drop_minute=111,max_drop_minute=202,min_feathers=12000,max_feathers=15000),
            TR_Expedition(lvl=21,seeds=12000,duration=369,name="The Western Wall",min_drop_minute=126,max_drop_minute=226,min_feathers=15000,max_feathers=18000),
            TR_Expedition(lvl=22,seeds=14000,duration=410,name="Giant's Causeway",min_drop_minute=141,max_drop_minute=249,min_feathers=18000,max_feathers=21000),
            TR_Expedition(lvl=23,seeds=16000,duration=447,name="The Grand Palace",min_drop_minute=156,max_drop_minute=273,min_feathers=21000,max_feathers=24000),
            TR_Expedition(lvl=24,seeds=18000,duration=480,name="Neuschwanstein Castle",min_drop_minute=171,max_drop_minute=297,min_feathers=24000,max_feathers=27000),
            TR_Expedition(lvl=25,seeds=20000,duration=511,name="Statue of Liberty",min_drop_minute=186,max_drop_minute=320,min_feathers=27000,max_feathers=30000),
            TR_Expedition(lvl=26,seeds=24000,duration=588,name="Ha Long Bay",min_drop_minute=201,max_drop_minute=344,min_feathers=33000,max_feathers=36000),
            TR_Expedition(lvl=27,seeds=28000,duration=659,name="Stonehenge",min_drop_minute=216,max_drop_minute=368,min_feathers=38000,max_feathers=43000),
            TR_Expedition(lvl=28,seeds=32000,duration=725,name="Mount Fuji",min_drop_minute=231,max_drop_minute=392,min_feathers=45000,max_feathers=49000),
            TR_Expedition(lvl=29,seeds=36000,duration=785,name="Petra",min_drop_minute=246,max_drop_minute=415,min_feathers=50000,max_feathers=60000),
            TR_Expedition(lvl=30,seeds=40000,duration=842,name="Kiribati",min_drop_minute=246,max_drop_minute=483,min_feathers=60000,max_feathers=70000),

            
            ])
