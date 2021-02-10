import { NgModule } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { CommonModule } from '@angular/common';


@NgModule({
  declarations: [
    HeaderComponent
  ],
  imports: [
    CommonModule,
  ],
  providers: [],
  bootstrap: [],
  exports: [
    HeaderComponent
  ],
})
export class UiModule { }
