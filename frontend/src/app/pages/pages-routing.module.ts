import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
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
