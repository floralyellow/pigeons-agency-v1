import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ExpeditionsComponent } from './components';
import { DashboardComponent } from './components/dashboard';
import { PagesComponent } from './pages.component';

const routes: Routes = [
  {
    path: '',
    component: PagesComponent, 
    children: [
      {
        path: '',
          children: [
            {
              path: 'index',
              component: DashboardComponent,
            },
            {
              path: 'expeditions',
              component: ExpeditionsComponent,
            },
            { 
              path: '',
              redirectTo: '/index',
              pathMatch: 'full' 
            },
          ]
      }
    ]
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule],
})
export class PagesRoutingModule { }
