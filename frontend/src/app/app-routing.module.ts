import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent, AuthentificationComponent } from './auth';
import { IsNotAuth,IsAuth } from './core/guards/';

const routes: Routes = [
  {
    path : "dashboard",
    component : RegisterComponent,
    canActivate : [IsAuth]
  },
  {
    path : "register",
    component : RegisterComponent,
    canActivate : [IsNotAuth]
  },
  {
    path : "authentification",
    component : AuthentificationComponent,
    canActivate : [IsNotAuth]
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
})
export class AppRoutingModule { }
