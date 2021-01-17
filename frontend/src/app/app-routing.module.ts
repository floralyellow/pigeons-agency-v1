import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent, AuthentificationComponent } from './auth';

const routes: Routes = [
  {
    path : "register",
    component : RegisterComponent
  },
  {
    path : "authentification",
    component : AuthentificationComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
