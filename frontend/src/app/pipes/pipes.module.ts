import { NgModule } from '@angular/core';
import { NumberToArrayPipe, SecondToMinPipe, ShortNumberPipe } from '.';
import { CommonModule } from '@angular/common';
import { FilterNotSoldPigeonPipe } from './filter-not-sold-pigeon.pipe';
@NgModule({
  declarations: [
    SecondToMinPipe,
    NumberToArrayPipe,
    ShortNumberPipe,
    FilterNotSoldPigeonPipe,
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
  ],
})
export class PipesModule { }
