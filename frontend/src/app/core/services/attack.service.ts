import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { User } from '../models/user';
import { Pigeon } from '../models';
import { Attack } from '../models/attack';

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

  postAttack(team : 'A'|'B', attackedUserId : number): Promise<{
    user: User, 
    users: User[], 
    attack:Attack, 
    attack_pigeons:Pigeon[], 
    defend_pigeons:Pigeon[]
  }> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/attack', `a_team=${team}&u_id=${attackedUserId}`)
        .subscribe((res: { 'message': { 
          user: User, 
          users: User[], 
          attack: Attack, 
          attack_pigeons:Pigeon[], 
          defend_pigeons:Pigeon[] 
        } }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
