import { NgModule } from '@angular/core';
import { DashboardComponent } from './components/dashboard/';
import { PagesComponent } from './pages.component';
import { PagesRoutingModule } from './pages-routing.module';
import { CommonModule } from '@angular/common';
import { UiModule } from '../ui/ui.module';

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
  providers: [],
  bootstrap: []
})
export class PagesModule { }
