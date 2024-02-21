from django.db import transaction

def remove_notifs(player):
    with transaction.atomic():
        player.nb_notifs = 0
        player.save   