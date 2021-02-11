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
from django.contrib.postgres.fields import ArrayField






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

        TR_Pigeon(lvl_expedition=1,coef_chance_rate=1,pigeon_type=1,src="furegeon.png",name="pig1-1",min_atk=1,max_atk=11,min_life=3,max_life=33,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=2,coef_chance_rate=1,pigeon_type=1,src="bombird.png",name="pig1-2",min_atk=8,max_atk=19,min_life=24,max_life=57,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=3,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-3",min_atk=15,max_atk=27,min_life=45,max_life=81,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=4,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-4",min_atk=22,max_atk=36,min_life=66,max_life=108,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=5,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-5",min_atk=29,max_atk=45,min_life=87,max_life=135,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=6,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-6",min_atk=37,max_atk=55,min_life=111,max_life=165,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=7,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-7",min_atk=46,max_atk=67,min_life=138,max_life=201,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=8,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-8",min_atk=57,max_atk=81,min_life=171,max_life=243,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=9,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-9",min_atk=70,max_atk=97,min_life=210,max_life=291,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=10,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-10",min_atk=85,max_atk=115,min_life=255,max_life=345,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=11,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-11",min_atk=101,max_atk=134,min_life=303,max_life=402,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=12,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-12",min_atk=119,max_atk=155,min_life=357,max_life=465,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=13,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-13",min_atk=138,max_atk=178,min_life=414,max_life=534,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=14,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-14",min_atk=160,max_atk=204,min_life=480,max_life=612,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=15,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-15",min_atk=184,max_atk=232,min_life=552,max_life=696,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=16,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-16",min_atk=211,max_atk=263,min_life=633,max_life=789,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=17,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-17",min_atk=240,max_atk=296,min_life=720,max_life=888,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=18,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-18",min_atk=271,max_atk=331,min_life=813,max_life=993,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=19,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-19",min_atk=305,max_atk=369,min_life=915,max_life=1107,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=20,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-20",min_atk=342,max_atk=410,min_life=1026,max_life=1230,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=21,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-21",min_atk=382,max_atk=454,min_life=1146,max_life=1362,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=22,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-22",min_atk=426,max_atk=502,min_life=1278,max_life=1506,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=23,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-23",min_atk=474,max_atk=554,min_life=1422,max_life=1662,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=24,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-24",min_atk=528,max_atk=612,min_life=1584,max_life=1836,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=25,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-25",min_atk=586,max_atk=674,min_life=1758,max_life=2022,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=26,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-26",min_atk=647,max_atk=739,min_life=1941,max_life=2217,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=27,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-27",min_atk=712,max_atk=808,min_life=2136,max_life=2424,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=28,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-28",min_atk=782,max_atk=882,min_life=2346,max_life=2646,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=29,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-29",min_atk=857,max_atk=962,min_life=2571,max_life=2886,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=30,coef_chance_rate=1,pigeon_type=1,src="test.png",name="pig1-30",min_atk=939,max_atk=1049,min_life=2817,max_life=3147,min_shield=0,max_shield=0,speed=50,min_luck_1=50,effect_1_chance=[1,1,1],effect_1=[1,2,3],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=1,coef_chance_rate=1,pigeon_type=2,src="pigetassium.png",name="pig2-1",min_atk=1,max_atk=11,min_life=3,max_life=33,min_shield=1,max_shield=3,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=2,coef_chance_rate=1,pigeon_type=2,src="rubygeon.png",name="pig2-2",min_atk=8,max_atk=19,min_life=24,max_life=57,min_shield=3,max_shield=5,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=3,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-3",min_atk=15,max_atk=27,min_life=45,max_life=81,min_shield=5,max_shield=7,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=4,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-4",min_atk=22,max_atk=36,min_life=66,max_life=108,min_shield=7,max_shield=10,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=5,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-5",min_atk=29,max_atk=45,min_life=87,max_life=135,min_shield=10,max_shield=12,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=6,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-6",min_atk=37,max_atk=55,min_life=111,max_life=165,min_shield=12,max_shield=15,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=7,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-7",min_atk=46,max_atk=67,min_life=138,max_life=201,min_shield=15,max_shield=19,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=8,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-8",min_atk=57,max_atk=81,min_life=171,max_life=243,min_shield=19,max_shield=23,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=9,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-9",min_atk=70,max_atk=97,min_life=210,max_life=291,min_shield=23,max_shield=28,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=10,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-10",min_atk=85,max_atk=115,min_life=255,max_life=345,min_shield=28,max_shield=34,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=11,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-11",min_atk=101,max_atk=134,min_life=303,max_life=402,min_shield=34,max_shield=40,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=12,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-12",min_atk=119,max_atk=155,min_life=357,max_life=465,min_shield=40,max_shield=46,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=13,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-13",min_atk=138,max_atk=178,min_life=414,max_life=534,min_shield=46,max_shield=53,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=14,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-14",min_atk=160,max_atk=204,min_life=480,max_life=612,min_shield=53,max_shield=61,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=15,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-15",min_atk=184,max_atk=232,min_life=552,max_life=696,min_shield=61,max_shield=70,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=16,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-16",min_atk=211,max_atk=263,min_life=633,max_life=789,min_shield=70,max_shield=80,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=17,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-17",min_atk=240,max_atk=296,min_life=720,max_life=888,min_shield=80,max_shield=90,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=18,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-18",min_atk=271,max_atk=331,min_life=813,max_life=993,min_shield=90,max_shield=102,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=19,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-19",min_atk=305,max_atk=369,min_life=915,max_life=1107,min_shield=102,max_shield=114,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=20,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-20",min_atk=342,max_atk=410,min_life=1026,max_life=1230,min_shield=114,max_shield=127,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=21,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-21",min_atk=382,max_atk=454,min_life=1146,max_life=1362,min_shield=127,max_shield=142,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=22,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-22",min_atk=426,max_atk=502,min_life=1278,max_life=1506,min_shield=142,max_shield=158,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=23,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-23",min_atk=474,max_atk=554,min_life=1422,max_life=1662,min_shield=158,max_shield=176,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=24,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-24",min_atk=528,max_atk=612,min_life=1584,max_life=1836,min_shield=176,max_shield=195,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=25,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-25",min_atk=586,max_atk=674,min_life=1758,max_life=2022,min_shield=195,max_shield=216,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=26,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-26",min_atk=647,max_atk=739,min_life=1941,max_life=2217,min_shield=216,max_shield=237,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=27,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-27",min_atk=712,max_atk=808,min_life=2136,max_life=2424,min_shield=237,max_shield=261,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=28,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-28",min_atk=782,max_atk=882,min_life=2346,max_life=2646,min_shield=261,max_shield=286,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=29,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-29",min_atk=857,max_atk=962,min_life=2571,max_life=2886,min_shield=286,max_shield=313,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
        TR_Pigeon(lvl_expedition=30,coef_chance_rate=1,pigeon_type=2,src="test.png",name="pig2-30",min_atk=939,max_atk=1049,min_life=2817,max_life=3147,min_shield=313,max_shield=0,speed=40,min_luck_1=70,effect_1_chance=[1,1,1],effect_1=[4,5,6],min_luck_2=80,effect_2_chance=[1,1],effect_2=[7,8],is_active=True),
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

        TR_Effect.objects.all().delete() 
        TR_Effect.objects.bulk_create([

        TR_Effect(effect_id=0,effect_name="none",is_active_effect=False,has_value=False,min_value=0,max_value=0,desc="No effect"),
        TR_Effect(effect_id=1,effect_name="Mountain Damage",is_active_effect=True,has_value=True,min_value=10,max_value=30,desc="More damage against Mountain"),
        TR_Effect(effect_id=2,effect_name="Forest Damage",is_active_effect=True,has_value=True,min_value=10,max_value=30,desc="More damage against Forest"),
        TR_Effect(effect_id=3,effect_name="Lake Damage",is_active_effect=True,has_value=True,min_value=10,max_value=30,desc="More damage against Lake"),
        TR_Effect(effect_id=4,effect_name="Mountain Support",is_active_effect=False,has_value=True,min_value=5,max_value=25,desc="Gives your Mountain allies more damage"),
        TR_Effect(effect_id=5,effect_name="Forest Support",is_active_effect=False,has_value=True,min_value=5,max_value=25,desc="Gives your Forest allies more damage"),
        TR_Effect(effect_id=6,effect_name="Lake Support",is_active_effect=False,has_value=True,min_value=5,max_value=25,desc="Gives your Lake allies more damage"),
        TR_Effect(effect_id=7,effect_name="Critical",is_active_effect=True,has_value=True,min_value=30,max_value=60,desc="Chance of critical hits"),
        TR_Effect(effect_id=8,effect_name="Shield Breaker",is_active_effect=True,has_value=False,min_value=0,max_value=0,desc="Ignores shield"),

        ])

        return JsonResponse({ "status": "ok" })