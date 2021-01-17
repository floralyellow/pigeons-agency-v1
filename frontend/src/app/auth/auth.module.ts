import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RegisterComponent } from './register/register.component';
import { AuthentificationComponent } from './authentification/authentification.component';


@NgModule({
  declarations: [
    RegisterComponent,
    AuthentificationComponent
  ],
  imports: [
    BrowserModule,
  ],
  providers: [
  ],
  bootstrap: [
  ],
  exports: [
    RegisterComponent,
    AuthentificationComponent
  ],
})
export class AuthModule { }
