import { AuthService } from '../services/auth.service';
import { ActivatedRouteSnapshot, createUrlTreeFromSnapshot } from '@angular/router';
import { inject } from '@angular/core';

export const IsNotAuth = (next: ActivatedRouteSnapshot) => {
  const isLoggedIn = inject(AuthService).checkIfLoggedIn();

  if (isLoggedIn) {
    createUrlTreeFromSnapshot(next, ['/'])
    return false;
  }

  return true;
};