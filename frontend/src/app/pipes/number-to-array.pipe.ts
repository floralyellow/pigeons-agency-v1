import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'numberToArray'
})
export class NumberToArrayPipe implements PipeTransform {

  transform(value: number): any[] {
    let generatedArray = [];
    for (let i = 0; i < value; i++) {
      generatedArray.push(0);
    }
    return generatedArray;
  }

}
