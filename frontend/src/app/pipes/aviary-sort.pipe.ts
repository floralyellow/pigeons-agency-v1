import { Pipe, PipeTransform } from '@angular/core';
import { Pigeon } from '../core/models';
import { SortEnum } from '../core/models/sort-enum';

@Pipe({
  name: 'aviarySort',
  pure: false
})
export class AviarySortPipe implements PipeTransform {

  transform(pigeonList: Pigeon[], sortBy: SortEnum): Pigeon[] {
    const notOpenPigeonList : Pigeon[] = pigeonList.filter((pigeon)=>pigeon.is_open === false)
    const orderedByList : Pigeon[] = pigeonList
    .filter((pigeon)=>pigeon.is_open)
    .sort((a,b) => {
      switch(sortBy) {
        case SortEnum.luckAndLevel: 
          const n = b.lvl - a.lvl;
          if (n !== 0) {
              return n;
          }
          return b.luck - a.luck;
        case SortEnum.attack: 
          return (b.phys_atk - a.phys_atk)
        case SortEnum.magic: 
          return (b.magic_atk - a.magic_atk)
        case SortEnum.droppings: 
          return (a.droppings_minute - b.droppings_minute)
        case SortEnum.feathers: 
          return (b.feathers - a.feathers)
        case SortEnum.shield: 
          return (b.shield - a.shield)
        case SortEnum.team_a: 
          const b_is_team_a = (b.is_in_team_A)? 1 : 0
          const a_is_team_a = (a.is_in_team_A)? 1 : 0
          return (b_is_team_a - a_is_team_a)
        case SortEnum.team_b: 
          const b_is_team_b = (b.is_in_team_B)? 1 : 0
          const a_is_team_b = (a.is_in_team_B)? 1 : 0
          return (b_is_team_b - a_is_team_b)
        case SortEnum.default: 
          return (Date.parse(b.creation_time.toString()) - Date.parse(a.creation_time.toString()))
      }
    })
    return (sortBy === SortEnum.default|| sortBy === undefined)? [...notOpenPigeonList, ...orderedByList] : [...orderedByList, ...notOpenPigeonList]
  }
}
