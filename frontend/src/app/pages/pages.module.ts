import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { UiModule } from '../ui/ui.module';
import { AuthInterceptor } from '../core/interceptors/auth-interceptor'
import { NotificationInterceptor } from '../core/interceptors/notification-interceptor'
import { PipesModule } from '../pipes/pipes.module';
import {
  ExpeditionsComponent,
  AviaryComponent,
  LeaderboardComponent,
  UpgradeComponent,
  DashboardComponent,
  AdventureComponent,
  AttackComponent,
  GlobalTutorialComponent,
  AttackTutorialComponent,
  MessagesComponent,
  AviaryTutorialComponent,
  UpgradeTutorialComponent,
  AdventureTutorialComponent
} from './components/';
import {
  ExpeditionsService,
  LeaderboardService,
  UpgradeService,
  PlayerService,
  PigeonsService,
  AttackService,
  AdventureService,
  MessagesService,

} from '../core/services';

@NgModule({
  declarations: [
    DashboardComponent,
    PagesComponent,
    ExpeditionsComponent,
    AviaryComponent,
    LeaderboardComponent,
    AdventureComponent,
    UpgradeComponent,
    AttackComponent,
    GlobalTutorialComponent,
    AttackTutorialComponent,
    MessagesComponent,
    AviaryTutorialComponent,
    UpgradeTutorialComponent,
    AdventureTutorialComponent
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    UiModule,
    HttpClientModule,
    PipesModule,
    FontAwesomeModule,
  ],
  providers: [
    PlayerService,
    ExpeditionsService,
    UpgradeService,
    LeaderboardService,
    PigeonsService,
    AdventureService,
    AttackService,
    MessagesService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: NotificationInterceptor, multi: true },
  ],
  bootstrap: []
})
export class PagesModule { }
