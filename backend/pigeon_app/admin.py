
from django.contrib import admin
from .models import Player
from .models import	Pigeon
from .models import	TR_Lvl_info

print("------"+"admin.py")
    
admin.site.register(Player)

admin.site.register(Pigeon)
admin.site.register(TR_Lvl_info)
