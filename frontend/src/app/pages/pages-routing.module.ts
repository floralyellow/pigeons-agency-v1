import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {
  ExpeditionsComponent,
  AdventureComponent,
  AviaryComponent,
  DashboardComponent,
  LeaderboardComponent,
  UpgradeComponent
} from './components';
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
            path: 'adventure',
            component: AdventureComponent,
          },
          {
            path: 'aviary',
            component: AviaryComponent,
          },
          {
            path: 'leaderboard',
            component: LeaderboardComponent,
          },
          {
            path: 'upgrade',
            component: UpgradeComponent,
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
