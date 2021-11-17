import { NgModule } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { CommonModule } from '@angular/common';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { RouterModule } from '@angular/router';
import { ExpeditionCooldownComponent } from './expedition-cooldown/';
import { ExpeditionCardComponent } from './expedition-card/';
import { DashboardCardComponent } from './dashboard-card/';
import { SecondToMinPipe } from './pipes';
import { PigeonCardComponent } from './pigeon-card/pigeon-card.component';

@NgModule({
  declarations: [
    SecondToMinPipe,
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent,
    DashboardCardComponent,
    PigeonCardComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [],
  exports: [
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent,
    DashboardCardComponent,
    PigeonCardComponent
  ],
})
export class UiModule { }
