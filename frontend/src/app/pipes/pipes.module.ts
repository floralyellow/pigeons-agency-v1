import { NgModule } from '@angular/core';
import { NumberToArrayPipe, SecondToMinPipe, ShortNumberPipe } from '.';
import { CommonModule } from '@angular/common';
import { FilterNotSoldPigeonPipe } from './filter-not-sold-pigeon.pipe';
import { AviarySortPipe } from './aviary-sort.pipe';
@NgModule({
  declarations: [
    SecondToMinPipe,
    NumberToArrayPipe,
    ShortNumberPipe,
    FilterNotSoldPigeonPipe,
    AviarySortPipe,
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
  ],
})
export class PipesModule { }
