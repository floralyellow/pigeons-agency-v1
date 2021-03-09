import { NgModule } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { CommonModule } from '@angular/common';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { RouterModule } from '@angular/router';
import { ExpeditionCooldownComponent } from './expedition-cooldown/';
import { ExpeditionCardComponent } from './expedition-card/';
import { DashboardCardComponent } from './dashboard-card/';
import { SecondToMinPipe } from './pipes';

@NgModule({
  declarations: [
    SecondToMinPipe,
    HeaderComponent,
    ExpeditionCooldownComponent,
    ExpeditionCardComponent,
    DashboardCardComponent
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
    DashboardCardComponent
  ],
})
export class UiModule { }
