import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../src/environments/environment';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  user: User;
  bus = new Subject<any>();

  constructor(public router: Router, private http: HttpClient) { }

  // notify subscribers when some values changed
  emitChange() {
    this.bus.next();
  }

  login(APIParameter: LoginAPIParameter): Promise<LoginAPIReturn> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/token/', APIParameter)
        .subscribe((res: LoginAPIReturn) => {
          this.updateToken(res.access);
          this.updateUser();
          this.router.navigate(['/index']);
          resolve(res);
        }, err => {
          reject(err);
        });
    });
  }

  register(APIParameter: RegisterAPIParameter): Promise<RegisterAPIReturn> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/users/', APIParameter)
        .subscribe((res: RegisterAPIReturn) => {
          resolve(res);
          this.login(APIParameter);
        }, err => {
          reject(err);
        });
    });
  }

  updateToken(token: string) {
    localStorage.setItem('token', token);
  }

  updateUser() {
    const token = localStorage.getItem('token');
    const helper = new JwtHelperService();

    if (token) {
      const decodedToken = helper.decodeToken(token);
      this.user = decodedToken.user;
    } else {
      this.user = null;
    }

    this.emitChange();
  }

  checkIfLoggedIn(): boolean {

    const token = localStorage.getItem('token');
    if (token) {
      const helper = new JwtHelperService();
      if (!helper.isTokenExpired(token)) {
        this.updateUser();
        return true;
      }
    }

    this.logout();
    return false;
  }

  logout() {
    localStorage.removeItem('token');
    this.user = null;
    this.router.navigate([
      { outlets: { primary: ['authentification'], tutorial: null } },
    ]);
    this.updateUser();
    this.emitChange();
  }
}

export interface LoginAPIParameter {
  username: string;
  password: string;
}

export interface LoginAPIReturn {
  access: string
}

export interface RegisterAPIParameter {
  username: string;
  password: string;
}

export interface RegisterAPIReturn {
  message: string;
  data: any;
}

export interface User {
  id: number;
  username: string;
}
