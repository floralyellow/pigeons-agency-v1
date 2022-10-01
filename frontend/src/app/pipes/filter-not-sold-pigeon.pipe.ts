import { Pipe, PipeTransform } from '@angular/core';
import { Pigeon } from '../core/models/pigeon';

@Pipe({
  name: 'filterNotSoldPigeon'
})
export class FilterNotSoldPigeonPipe implements PipeTransform {

  transform(value: Pigeon[]): Pigeon[] {
    return value.filter(pigeon => {
      pigeon.is_sold === false
    });
  }
}
