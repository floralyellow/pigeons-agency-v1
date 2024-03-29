import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthentificationComponent } from './auth';
import { IsAuth } from './core/guards/';

const routes: Routes = [
  {
    path: "authentification",
    component: AuthentificationComponent
  },
  {
    path: "",
    canActivate: [IsAuth],
    loadChildren: () => import('./pages/pages.module').then(m => m.PagesModule),
  },
  {
    path: '',
    redirectTo: '/index',
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      routes,
      {
    enableTracing: false
}
    )
  ],
  exports: [RouterModule],
})
export class AppRoutingModule { }
