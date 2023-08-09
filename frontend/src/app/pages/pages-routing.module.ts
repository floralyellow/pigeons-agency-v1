import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {
  ExpeditionsComponent,
  AdventureComponent,
  AviaryComponent,
  DashboardComponent,
  LeaderboardComponent,
  UpgradeComponent,
  AttackComponent,
  AttackTutorialComponent,
  GlobalTutorialComponent,
  ExpeditionAviaryTutorialComponent
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
            path: 'attack',
            component: AttackComponent,
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
          { path: 'global-tutorial', component: GlobalTutorialComponent, outlet: 'tutorial' },
          { path: 'expedition-aviary-tutorial', component: ExpeditionAviaryTutorialComponent, outlet: 'tutorial' },
          { path: 'attack-tutorial', component: AttackTutorialComponent, outlet: 'tutorial' },
          {
            path: '',
            redirectTo: '/global-tutorial',
            pathMatch: 'full',
            outlet: 'tutorial'
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
