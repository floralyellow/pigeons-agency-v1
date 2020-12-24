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
            TR_Lvl_info(lvl=1,seeds_minute = 60,max_seeds=60,max_droppings=30,max_feathers=35),
            TR_Lvl_info(lvl=2,seeds_minute = 90, max_seeds=90,max_droppings=60,max_feathers=70),
        ])

        TR_Pigeon.objects.all().delete() 

        TR_Pigeon.objects.bulk_create([
            TR_Pigeon(lvl_expedition=1,coef_chance_rate=1,pigeon_type=1,name='first',min_atk=2,max_atk=5,min_life=6,max_life=10,min_shield=0,max_shield=0,speed=10),
            TR_Pigeon(lvl_expedition=1,coef_chance_rate=3,pigeon_type=1,name='second',min_atk=5,max_atk=20,min_life=10,max_life=30,min_shield=1,max_shield=2,speed=15),
        ])

        TR_Expedition.objects.all().delete() 

        TR_Expedition.objects.bulk_create([
            TR_Expedition(lvl=1,seeds=2,duration=5,name="Garden Run"),
            TR_Expedition(lvl=2,seeds=4,duration=8,name="Yee"),
        ])
   
        return JsonResponse({ "status": "ok" })