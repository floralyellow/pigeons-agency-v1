import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets

from ..models import Player
from ..models.player import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """model view set that generate automaticly get,post,patch, delete on User model"""

    serializer_class = UserSerializer
    queryset = User.objects.none()

    def get_queryset(self):
        """queryset = all for GET and queryset = request.user.id for other action
        player can get all Users infos but not modify"""
        queryset = self.queryset
        if self.request.method == "GET":
            query_set = User.objects.filter(is_staff=False)
            return query_set
        query_set = queryset.filter(id=self.request.user.id)
        return query_set

    def get_permissions(self):
        """Allow anonymous users to post user"""
        logging.debug(str(self.request.method))

        if self.request.method == "POST":
            return []
        return super().get_permissions()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """signal receiver that create a player to every assosciated created User"""
    if created:
        Player.objects.create(user=instance)
