import { AuthService } from '../services/auth.service';
import { Router, CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class IsNotAuth implements CanActivate {

    constructor(public router: Router, private auth: AuthService) { }

    canActivate(): boolean {
        const isLoggedIn = this.auth.checkIfLoggedIn();

        if (isLoggedIn) {
            this.router.navigate(['/index']);
            return false;
        }

        return true;
    }
}