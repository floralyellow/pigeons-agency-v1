import random

from django.core.management.base import BaseCommand

from ...models import PvePigeon, TR_Expedition, TR_Pigeon


class Command(BaseCommand):
    help = "Create pigeons that will be used for adventure & events"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("--force_recreate", type=str)

    def handle(self, *args, **kwargs):
        LVL_RANGE = range(1, 30 + 1)
        PIGEON_TYPES_RANGE = range(1, 3 + 1)
        LUCK_VALUES_RANGE = [20, 40, 60, 80, 90, 95, 100]

        if PvePigeon.objects.count() == 0 or kwargs["force_recreate"] == "TRUE":
            PvePigeon.objects.all().delete()

            for lvl in LVL_RANGE:
                for pigeon_type in PIGEON_TYPES_RANGE:
                    for luck_value in LUCK_VALUES_RANGE:
                        expedition = TR_Expedition.objects.filter(lvl=lvl)[0]

                        p = TR_Pigeon.objects.filter(
                            lvl_expedition=expedition.lvl, pigeon_type=pigeon_type
                        )[0]

                        phys_atk = (
                            round(luck_value / 100 * (p.max_phys_atk - p.min_phys_atk))
                            + p.min_phys_atk
                        )
                        magic_atk = (
                            round(luck_value / 100 * (p.max_magic_atk - p.min_magic_atk))
                            + p.min_magic_atk
                        )
                        shield = (
                            round(luck_value / 100 * (p.max_shield - p.min_shield)) + p.min_shield
                        )
                        drop_min = (
                            round(
                                luck_value
                                / 100
                                * (expedition.max_drop_minute - expedition.min_drop_minute)
                            )
                            + expedition.min_drop_minute
                        )
                        feathers = (
                            round(
                                luck_value
                                / 100
                                * (expedition.max_feathers - expedition.min_feathers)
                            )
                            + expedition.min_feathers
                        )

                        # only used to have previous lvl src
                        previous_lvl_pigeon = TR_Pigeon.objects.filter(
                            lvl_expedition=max(expedition.lvl - 1, 1), pigeon_type=pigeon_type
                        )[0]
                        random_src = random.randint(0, len(previous_lvl_pigeon.src) - 1)

                        new_pve_pigeon = PvePigeon(
                            player_id=-1,
                            pigeon_type=p.pigeon_type,
                            name=previous_lvl_pigeon.name[random_src],
                            src=previous_lvl_pigeon.src[random_src],
                            pigeon_id=p.pigeon_id,
                            luck=luck_value,
                            lvl=expedition.lvl,
                            phys_atk=phys_atk,
                            magic_atk=magic_atk,
                            shield=shield,
                            droppings_minute=drop_min,
                            feathers=feathers,
                        )

                        new_pve_pigeon.save()
