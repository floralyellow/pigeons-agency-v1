from django.http import JsonResponse
import logging
from rest_framework.views import APIView
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Effect
from ..models import TR_Expedition





class FillTRView(APIView):
    # create pigeon
    def post(self, request):
        TR_Lvl_info.objects.all().delete() 
        TR_Lvl_info.objects.bulk_create([

        TR_Lvl_info(lvl=1,seeds_minute=75,max_seeds=25,max_droppings=70,max_feathers=15,max_pigeons=10),
        TR_Lvl_info(lvl=2,seeds_minute=100,max_seeds=50,max_droppings=162,max_feathers=60,max_pigeons=12),
        TR_Lvl_info(lvl=3,seeds_minute=150,max_seeds=110,max_droppings=392,max_feathers=240,max_pigeons=14),
        TR_Lvl_info(lvl=4,seeds_minute=250,max_seeds=220,max_droppings=720,max_feathers=720,max_pigeons=16),
        TR_Lvl_info(lvl=5,seeds_minute=350,max_seeds=420,max_droppings=1035,max_feathers=1440,max_pigeons=18),
        TR_Lvl_info(lvl=6,seeds_minute=450,max_seeds=950,max_droppings=1600,max_feathers=2610,max_pigeons=20),
        TR_Lvl_info(lvl=7,seeds_minute=550,max_seeds=1600,max_droppings=2200,max_feathers=4650,max_pigeons=22),
        TR_Lvl_info(lvl=8,seeds_minute=650,max_seeds=2600,max_droppings=3120,max_feathers=8250,max_pigeons=24),
        TR_Lvl_info(lvl=9,seeds_minute=750,max_seeds=4100,max_droppings=4225,max_feathers=14250,max_pigeons=26),
        TR_Lvl_info(lvl=10,seeds_minute=850,max_seeds=6100,max_droppings=5530,max_feathers=22500,max_pigeons=28),
        TR_Lvl_info(lvl=11,seeds_minute=950,max_seeds=8400,max_droppings=6900,max_feathers=33000,max_pigeons=30),
        TR_Lvl_info(lvl=12,seeds_minute=1050,max_seeds=12800,max_droppings=8560,max_feathers=46500,max_pigeons=32),
        TR_Lvl_info(lvl=13,seeds_minute=1150,max_seeds=15900,max_droppings=10370,max_feathers=63000,max_pigeons=34),
        TR_Lvl_info(lvl=14,seeds_minute=1250,max_seeds=19600,max_droppings=12420,max_feathers=84000,max_pigeons=36),
        TR_Lvl_info(lvl=15,seeds_minute=1350,max_seeds=23300,max_droppings=15770,max_feathers=111000,max_pigeons=38),
        TR_Lvl_info(lvl=16,seeds_minute=1450,max_seeds=28200,max_droppings=19200,max_feathers=145500,max_pigeons=40),
        TR_Lvl_info(lvl=17,seeds_minute=1550,max_seeds=32900,max_droppings=22890,max_feathers=187500,max_pigeons=42),
        TR_Lvl_info(lvl=18,seeds_minute=1650,max_seeds=38000,max_droppings=26950,max_feathers=240000,max_pigeons=44),
        TR_Lvl_info(lvl=19,seeds_minute=1750,max_seeds=42800,max_droppings=31165,max_feathers=315000,max_pigeons=46),
        TR_Lvl_info(lvl=20,seeds_minute=1850,max_seeds=48000,max_droppings=37560,max_feathers=405000,max_pigeons=48),
        TR_Lvl_info(lvl=21,seeds_minute=1950,max_seeds=66000,max_droppings=44000,max_feathers=495000,max_pigeons=50),
        TR_Lvl_info(lvl=22,seeds_minute=2050,max_seeds=78000,max_droppings=50700,max_feathers=585000,max_pigeons=52),
        TR_Lvl_info(lvl=23,seeds_minute=2150,max_seeds=90000,max_droppings=57915,max_feathers=675000,max_pigeons=54),
        TR_Lvl_info(lvl=24,seeds_minute=2250,max_seeds=102000,max_droppings=65520,max_feathers=765000,max_pigeons=56),
        TR_Lvl_info(lvl=25,seeds_minute=2350,max_seeds=114000,max_droppings=73370,max_feathers=855000,max_pigeons=58),
        TR_Lvl_info(lvl=26,seeds_minute=2450,max_seeds=138000,max_droppings=81750,max_feathers=1035000,max_pigeons=60),
        TR_Lvl_info(lvl=27,seeds_minute=2550,max_seeds=162000,max_droppings=90520,max_feathers=1215000,max_pigeons=62),
        TR_Lvl_info(lvl=28,seeds_minute=2650,max_seeds=186000,max_droppings=99680,max_feathers=1410000,max_pigeons=64),
        TR_Lvl_info(lvl=29,seeds_minute=2750,max_seeds=210000,max_droppings=109065,max_feathers=1650000,max_pigeons=66),
        TR_Lvl_info(lvl=30,seeds_minute=2850,max_seeds=230000,max_droppings=123930,max_feathers=1950000,max_pigeons=68),
        
        ])

        TR_Pigeon.objects.all().delete() 
        TR_Pigeon.objects.bulk_create([
        
        TR_Pigeon(lvl_expedition=1,coef_chance_rate=1,pigeon_type=1,name='first',min_atk=2,max_atk=5,min_life=6,max_life=10,min_shield=0,max_shield=0,speed=10),
        TR_Pigeon(lvl_expedition=1,coef_chance_rate=3,pigeon_type=1,name='second',min_atk=5,max_atk=20,min_life=10,max_life=30,min_shield=1,max_shield=2,speed=15),
        TR_Pigeon(lvl_expedition=2,coef_chance_rate=1,pigeon_type=1,name='third',min_atk=20,max_atk=50,min_life=6,max_life=10,min_shield=0,max_shield=0,speed=10),
        TR_Pigeon(lvl_expedition=2,coef_chance_rate=3,pigeon_type=1,name='fourth',min_atk=50,max_atk=200,min_life=10,max_life=30,min_shield=1,max_shield=2,speed=15),
        
        ])

        TR_Expedition.objects.all().delete() 
        TR_Expedition.objects.bulk_create([

        TR_Expedition(lvl=1,seeds=10,duration=8,name="Expedition1",min_drop_minute=1,max_drop_minute=6,min_feathers=2,max_feathers=4),
        TR_Expedition(lvl=2,seeds=20,duration=12,name="Expedition2",min_drop_minute=3,max_drop_minute=6,min_feathers=4,max_feathers=8),
        TR_Expedition(lvl=3,seeds=40,duration=16,name="Expedition3",min_drop_minute=5,max_drop_minute=9,min_feathers=8,max_feathers=16),
        TR_Expedition(lvl=4,seeds=80,duration=19,name="Expedition4",min_drop_minute=7,max_drop_minute=11,min_feathers=16,max_feathers=32),
        TR_Expedition(lvl=5,seeds=150,duration=26,name="Expedition5",min_drop_minute=9,max_drop_minute=14,min_feathers=32,max_feathers=64),
        TR_Expedition(lvl=6,seeds=270,duration=36,name="Expedition6",min_drop_minute=12,max_drop_minute=20,min_feathers=64,max_feathers=110),
        TR_Expedition(lvl=7,seeds=450,duration=49,name="Expedition7",min_drop_minute=16,max_drop_minute=24,min_feathers=110,max_feathers=200),
        TR_Expedition(lvl=8,seeds=700,duration=65,name="Expedition8",min_drop_minute=20,max_drop_minute=32,min_feathers=200,max_feathers=350),
        TR_Expedition(lvl=9,seeds=1100,duration=88,name="Expedition9",min_drop_minute=24,max_drop_minute=41,min_feathers=350,max_feathers=600),
        TR_Expedition(lvl=10,seeds=1600,duration=113,name="Expedition10",min_drop_minute=28,max_drop_minute=51,min_feathers=600,max_feathers=900),
        TR_Expedition(lvl=11,seeds=2200,duration=139,name="Expedition11",min_drop_minute=32,max_drop_minute=60,min_feathers=900,max_feathers=1300),
        TR_Expedition(lvl=12,seeds=2850,duration=163,name="Expedition12",min_drop_minute=37,max_drop_minute=70,min_feathers=1300,max_feathers=1800),
        TR_Expedition(lvl=13,seeds=3500,duration=183,name="Expedition13",min_drop_minute=42,max_drop_minute=80,min_feathers=1800,max_feathers=2400),
        TR_Expedition(lvl=14,seeds=4250,duration=204,name="Expedition14",min_drop_minute=47,max_drop_minute=91,min_feathers=2400,max_feathers=3200),
        TR_Expedition(lvl=15,seeds=5000,duration=222,name="Expedition15",min_drop_minute=57,max_drop_minute=109,min_feathers=3200,max_feathers=4200),
        TR_Expedition(lvl=16,seeds=6000,duration=248,name="Expedition16",min_drop_minute=67,max_drop_minute=125,min_feathers=4200,max_feathers=5500),
        TR_Expedition(lvl=17,seeds=7000,duration=271,name="Expedition17",min_drop_minute=77,max_drop_minute=141,min_feathers=5500,max_feathers=7000),
        TR_Expedition(lvl=18,seeds=8000,duration=291,name="Expedition18",min_drop_minute=87,max_drop_minute=158,min_feathers=7000,max_feathers=9000),
        TR_Expedition(lvl=19,seeds=9000,duration=309,name="Expedition19",min_drop_minute=97,max_drop_minute=174,min_feathers=9000,max_feathers=12000),
        TR_Expedition(lvl=20,seeds=10000,duration=324,name="Expedition20",min_drop_minute=111,max_drop_minute=202,min_feathers=12000,max_feathers=15000),
        TR_Expedition(lvl=21,seeds=12000,duration=369,name="Expedition21",min_drop_minute=126,max_drop_minute=226,min_feathers=15000,max_feathers=18000),
        TR_Expedition(lvl=22,seeds=14000,duration=410,name="Expedition22",min_drop_minute=141,max_drop_minute=249,min_feathers=18000,max_feathers=21000),
        TR_Expedition(lvl=23,seeds=16000,duration=447,name="Expedition23",min_drop_minute=156,max_drop_minute=273,min_feathers=21000,max_feathers=24000),
        TR_Expedition(lvl=24,seeds=18000,duration=480,name="Expedition24",min_drop_minute=171,max_drop_minute=297,min_feathers=24000,max_feathers=27000),
        TR_Expedition(lvl=25,seeds=20000,duration=511,name="Expedition25",min_drop_minute=186,max_drop_minute=320,min_feathers=27000,max_feathers=30000),
        TR_Expedition(lvl=26,seeds=24000,duration=588,name="Expedition26",min_drop_minute=201,max_drop_minute=344,min_feathers=33000,max_feathers=36000),
        TR_Expedition(lvl=27,seeds=28000,duration=659,name="Expedition27",min_drop_minute=216,max_drop_minute=368,min_feathers=38000,max_feathers=43000),
        TR_Expedition(lvl=28,seeds=32000,duration=725,name="Expedition28",min_drop_minute=231,max_drop_minute=392,min_feathers=45000,max_feathers=49000),
        TR_Expedition(lvl=29,seeds=36000,duration=785,name="Expedition29",min_drop_minute=246,max_drop_minute=415,min_feathers=50000,max_feathers=60000),
        TR_Expedition(lvl=30,seeds=40000,duration=842,name="Expedition30",min_drop_minute=246,max_drop_minute=483,min_feathers=60000,max_feathers=70000),
        
        ])

        return JsonResponse({ "status": "ok" })