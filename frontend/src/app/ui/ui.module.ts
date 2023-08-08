import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { ExpeditionCooldownComponent } from './expedition-cooldown/';
import { ExpeditionCardComponent } from './expedition-card/';
import { DashboardCardComponent } from './dashboard-card/';
import { HeaderComponent } from './header/';
import { AdventureCardComponent } from './adventure-card/';
import { PigeonCardComponent } from './pigeon-card/';

import { PipesModule } from '../pipes/pipes.module';
import { PigeonCardHeaderComponent } from './pigeon-card-header/pigeon-card-header.component';
import { ModalComponent } from './modal/modal.component';
import { AttackPigeonComponent } from './attack-pigeon/attack-pigeon.component';

@NgModule({
  declarations: [
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent,
    DashboardCardComponent,
    PigeonCardComponent,
    AdventureCardComponent,
    PigeonCardHeaderComponent,
    ModalComponent,
    AttackPigeonComponent
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
    PigeonCardComponent,
    AdventureCardComponent,
    PigeonCardHeaderComponent,
    ModalComponent,
    AttackPigeonComponent
  ],
})
export class UiModule { }
