# from django.db.models.signals import post_save, pre_save
# from datetime import datetime, timezone
# from django.dispatch import receiver    
# from .models import Player
# from .services import update_service
# from django.contrib.auth.models import User
# from django.utils.functional import SimpleLazyObject
# import logging

# # not working
# def get_actual_value(request):
#     if request.user is None:
#         return None
#     return request.user #here should have value, so any code using request.user will work

# class UpdatePlayerMiddleware:
#     '''middleware qui intercepte toute les requêtes et met a jour player (seeds,droppings)'''
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
        
#     @receiver(pre_save, sender=Player)
#     def pre_save_player(sender, instance,**kwargs):
#         '''update player.last_updated_at to now()'''
#         instance.last_updated_at = datetime.now(timezone.utc)
    
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         user = SimpleLazyObject(lambda: get_actual_value(request))
#         logging.debug(str(user))
#         response = self.get_response(request)
#         logging.debug(str(request.user))

#         if user.is_authenticated:
#             logging.debug('yeeeee')
#             update_service.update_user_values(request.user)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

