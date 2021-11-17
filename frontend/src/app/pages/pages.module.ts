import { NgModule } from '@angular/core';
import { DashboardComponent } from './components/dashboard/';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { CommonModule } from '@angular/common';
import { UiModule } from '../ui/ui.module';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import {AuthInterceptor} from '../core/interceptors/auth-interceptor'
import { PlayerService } from '../core/services/player.service';
import { ShortNumberPipe } from './pipes/short-number.pipe';
import { ExpeditionsComponent } from './components/expeditions/';
import { ExpeditionsService } from '../core/services';
import { AviaryComponent } from './components/aviary/aviary.component';

@NgModule({
  declarations: [
    DashboardComponent,
    PagesComponent,
    ShortNumberPipe,
    ExpeditionsComponent,
    AviaryComponent,
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    UiModule,
    HttpClientModule
  ],
  providers: [
    PlayerService,
    ExpeditionsService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: []
})
export class PagesModule { }
