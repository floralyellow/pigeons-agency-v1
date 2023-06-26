import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class AttackService {

  constructor(private http: HttpClient) { }

  getUsers(): Promise<{ user: User, users: User[] }> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/attacklist')
        .subscribe((res: { 'message': { user: User, users: User[] } }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
