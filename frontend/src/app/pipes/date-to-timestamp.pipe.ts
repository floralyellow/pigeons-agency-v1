import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'dateToTimestamp'
})
export class DateToTimestampPipe implements PipeTransform {

  transform(date: Date): number {
    return date.getTime();
  }

}
