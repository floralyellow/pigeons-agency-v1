import { Pipe, PipeTransform } from '@angular/core';
import { Pigeon } from '../core/models';
import { SortEnum } from '../core/models/sort-enum';

@Pipe({
  name: 'aviarySort',
  pure: false
})
export class AviarySortPipe implements PipeTransform {

  transform(pigeonList: Pigeon[], sortBy: SortEnum): Pigeon[] {
    const notOpenPigeonList: Pigeon[] = pigeonList.filter((pigeon) => pigeon.is_open === false)
    const orderedByList: Pigeon[] = pigeonList
      .filter((pigeon) => pigeon.is_open)
      .sort((a, b) => {
        const bIsInTeam = (b.is_in_team_A || b.is_in_team_B) ? 1 : 0
        const aIsInTeam = (a.is_in_team_A || a.is_in_team_B) ? 1 : 0
        const levelDiff = b.lvl - a.lvl;
        const attackDiff = b.phys_atk - a.phys_atk;
        const magicDiff = b.magic_atk - a.magic_atk;
        const luckDiff = b.luck - a.luck;
        const droppingDiff = a.droppings_minute - b.droppings_minute;
        const teamDiff = bIsInTeam - aIsInTeam;
        const featherDiff = b.feathers - a.feathers;
        const shieldFiff = b.shield - a.shield;
        switch (sortBy) {
          case SortEnum.luckAndLevel:
            if (levelDiff !== 0) {
              return levelDiff;
            }
            return (luckDiff)
          case SortEnum.attack:
            return (attackDiff)
          case SortEnum.magic:
            return (magicDiff)
          case SortEnum.droppings:
            return (droppingDiff)
          case SortEnum.feathers:
            return (featherDiff)
          case SortEnum.shield:
            if (shieldFiff !== 0) {
              return shieldFiff;
            }
            return (magicDiff)
          case SortEnum.team_a:
            const b_is_team_a = (b.is_in_team_A) ? 1 : 0
            const a_is_team_a = (a.is_in_team_A) ? 1 : 0
            return (b_is_team_a - a_is_team_a)
          case SortEnum.team_b:
            const b_is_team_b = (b.is_in_team_B) ? 1 : 0
            const a_is_team_b = (a.is_in_team_B) ? 1 : 0
            return (b_is_team_b - a_is_team_b)
        }
      })
    return (sortBy === SortEnum.default || sortBy === undefined) ?
      pigeonList.sort((a, b) => (
        Date.parse(b.creation_time.toString()) - Date.parse(a.creation_time.toString())
      )) : [...orderedByList, ...notOpenPigeonList]
  }
}
