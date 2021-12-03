from django.contrib.postgres.fields import ArrayField
from django.core.management.base import BaseCommand

from ...models import TR_Expedition, Pigeon,Player
from ...services import pigeon_service


class Command(BaseCommand):
    help = 'Create pigeons that will be used for adventure & events'

    def add_arguments(self, parser):
        # Positional arguments
       parser.add_argument('--force_recreate', type=str)

    def handle(self, *args, **kwargs):

        if Pigeon.objects.filter(player_id=-1).count() == 0 or kwargs['force_recreate'] == 'TRUE':
            lvl = models.IntegerField(default=1)
    seeds = models.IntegerField(default=15)
    droppings = models.IntegerField(default=0)
    feathers = models.IntegerField(default=0)
    military_score = models.IntegerField(default=0)
    last_attacked = models.IntegerField(default=-1)
    time_last_attack = models.DateTimeField(auto_now_add=True, null=True)
    last_connected_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
            Player
            Pigeon.objects.filter(player_id=-1).delete()


            for lvl in range(1,30+1):
                for type in range(1,4+1):
                    for luck in [20,40,60,80,90,95]:
                        expedition = TR_Expedition.objects.filter(lvl=lvl)[0]
                        pigeon_service.add_pigeon(-1, expedition, type, luck)

