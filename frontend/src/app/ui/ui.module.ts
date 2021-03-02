import { NgModule } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { CommonModule } from '@angular/common';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { RouterModule } from '@angular/router';
import { ExpeditionCooldownComponent } from './expedition-cooldown/expedition-cooldown.component';
import { ExpeditionCardComponent } from './expedition-card/expedition-card.component';


@NgModule({
  declarations: [
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent
  ],
  imports: [
    RouterModule,
    CommonModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [],
  exports: [
    HeaderComponent
  ],
})
export class UiModule { }
