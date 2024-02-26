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
  ExpeditionTutorialComponent,
  MessagesComponent,
  UpgradeTutorialComponent,
  AviaryTutorialComponent,
  AdventureTutorialComponent
} from './components';
import { PagesComponent } from './pages.component';
import { IsAuth } from '../core/guards/';

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
            canActivate: [IsAuth],
          },
          {
            path: 'expeditions',
            component: ExpeditionsComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'adventure',
            component: AdventureComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'attack',
            component: AttackComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'aviary',
            component: AviaryComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'history',
            component: MessagesComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'leaderboard',
            component: LeaderboardComponent,
            canActivate: [IsAuth],
          },
          {
            path: 'upgrade',
            component: UpgradeComponent,
            canActivate: [IsAuth],
          },
          {
            path: '',
            redirectTo: '/index',
            pathMatch: 'full'
          },
          { path: 'global-tutorial', component: GlobalTutorialComponent, outlet: 'tutorial' },
          { path: 'expedition-tutorial', component: ExpeditionTutorialComponent, outlet: 'tutorial' },
          { path: 'attack-tutorial', component: AttackTutorialComponent, outlet: 'tutorial' },
          { path: 'upgrade-tutorial', component: UpgradeTutorialComponent, outlet: 'tutorial' },
          { path: 'aviary-tutorial', component: AviaryTutorialComponent, outlet: 'tutorial' },
          { path: 'adventure-tutorial', component: AdventureTutorialComponent, outlet: 'tutorial' },
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
