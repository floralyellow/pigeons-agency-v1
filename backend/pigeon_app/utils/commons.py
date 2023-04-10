from ..models import Pigeon

ATTACK_VARIANCE = 15

DELAY_SECONDS_BETWEEN_ATTACKS = 2 * 60  # 2 min

ADVENTURE_RATIO_REWARDS = 0.4

PROTECTED_UNTIL_MINUTES = 20

NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO = 0.25


def get_total_score(
    total_phys: int, total_magic: int, sum_shield_opponent: int, total_blocs_opponent: int
) -> int:
    return total_phys + total_magic - min((sum_shield_opponent * total_blocs_opponent), total_phys)


def get_pigeon_team(user_id: int, team: str):
    if team == "A":
        pigeons = Pigeon.objects.filter(player_id=user_id, is_in_team_A=True)
    elif team == "B":
        pigeons = Pigeon.objects.filter(player_id=user_id, is_in_team_B=True)
    return pigeons
