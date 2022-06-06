import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
  name: 'secondToMin'
})
export class SecondToMinPipe implements PipeTransform {
    transform(value: number): string {
       const minutes: number = Math.floor(value / 60);
       const seconde : number = (value - minutes * 60);
       if(minutes < 10){
         if(seconde < 10){
          return '0' + minutes + ':' + '0' + seconde;
         }
         return '0' + minutes + ':' + seconde;
       }
       else{
        if(seconde < 10){
         return minutes + ':' + '0' + seconde;
        }
        return + minutes + ':' + seconde;
       }
    }
}