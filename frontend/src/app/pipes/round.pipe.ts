import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'roundPipe'
})
export class RoundPipe implements PipeTransform {

  transform(value: number): number {
    return Math.round(value);
  }

}
