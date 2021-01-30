import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AuthentificationComponent } from './authentification/authentification.component';
import { CardComponent } from './ui/card/card.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AuthentificationComponent,
    CardComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule
  ],
  providers: [
  ],
  bootstrap: [
  ],
  exports: [
    AuthentificationComponent
  ],
})
export class AuthModule { }
