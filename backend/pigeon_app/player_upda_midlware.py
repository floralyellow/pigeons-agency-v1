from django.db.models.signals import post_save, pre_save
from datetime import datetime, timezone
from django.dispatch import receiver    
from .models import Player
from .services import update_service
from django.contrib.auth.models import User
import logging

class UpdatePlayerMiddleware:
    '''middleware qui intercepte toute les requêtes et met a jour player (seeds,droppings)'''
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        
    @receiver(pre_save, sender=Player)
    def pre_save_player(sender, instance,**kwargs):
        '''update player.last_updated_at to now()'''
        instance.last_updated_at = datetime.now(timezone.utc)

        
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        logging.debug(str(request.user))

        if request.user.is_authenticated:
            update_service.update_user_values(request.user)

        # Code to be executed for each request/response after
        # the view is called.

        return response

