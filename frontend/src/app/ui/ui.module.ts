import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { ExpeditionCooldownComponent } from './expedition-cooldown/';
import { ExpeditionCardComponent } from './expedition-card/';
import { DashboardCardComponent } from './dashboard-card/';
import { HeaderComponent } from './header/header.component';
import { PigeonCardComponent } from './pigeon-card/pigeon-card.component';

import { PipesModule } from '../pipes/pipes.module';

@NgModule({
  declarations: [
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent,
    DashboardCardComponent,
    PigeonCardComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    FontAwesomeModule,
    PipesModule
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
