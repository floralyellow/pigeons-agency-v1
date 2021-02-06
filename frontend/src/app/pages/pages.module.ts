import { NgModule } from '@angular/core';
import { DashboardComponent } from './components/dashboard/';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { CommonModule } from '@angular/common';
import { UiModule } from '../ui/ui.module';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import {AuthInterceptor} from '../core/interceptors/auth-interceptor'

@NgModule({
  declarations: [
    DashboardComponent,
    PagesComponent,
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    UiModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: []
})
export class PagesModule { }
