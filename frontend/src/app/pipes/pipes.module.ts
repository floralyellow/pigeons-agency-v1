import { NgModule } from '@angular/core';
import { NumberToArrayPipe, SecondToMinPipe, ShortNumberPipe } from '.';
import { CommonModule } from '@angular/common';
import { FilterNotSoldPigeonPipe } from './filter-not-sold-pigeon.pipe';
import { AviarySortPipe } from './aviary-sort.pipe';
import { DateToTimestampPipe } from './date-to-timestamp.pipe';
@NgModule({
  declarations: [
    SecondToMinPipe,
    NumberToArrayPipe,
    ShortNumberPipe,
    FilterNotSoldPigeonPipe,
    AviarySortPipe,
    DateToTimestampPipe,
  ],
  imports: [
    CommonModule,
  ],
  providers: [],
  bootstrap: [],
  exports: [
    SecondToMinPipe,
    NumberToArrayPipe,
    ShortNumberPipe,
    FilterNotSoldPigeonPipe,
    AviarySortPipe,
    DateToTimestampPipe,
  ],
})
export class PipesModule { }
