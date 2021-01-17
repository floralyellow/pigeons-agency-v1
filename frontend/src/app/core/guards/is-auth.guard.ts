import { AuthService } from './../services/auth.service';
import { Router, CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class IsAuth implements CanActivate {

    constructor(public router: Router, private AuthService: AuthService) { }

    canActivate(): boolean {
        const isLoggedIn = this.AuthService.checkIfLoggedIn();

        if (!isLoggedIn) {
            this.router.navigate(['/authentification']);
            return false;
        }

        return true;
    }
}