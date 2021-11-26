import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ExpeditionsComponent } from './components';
import { AviaryComponent } from './components/aviary/aviary.component';
import { DashboardComponent } from './components/dashboard';
import { LeaderboardComponent } from './components/leaderboard';
import { UpgradeComponent } from './components/upgrade/upgrade.component';
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
