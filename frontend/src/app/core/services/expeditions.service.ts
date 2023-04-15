import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Expedition, User } from '../models';
import { Aviary } from '../models/aviary';
import { Pigeon } from '../models/pigeon';

@Injectable({
  providedIn: 'root'
})
export class ExpeditionsService {

  constructor(private http: HttpClient) { }
  getExpeditionInfo(): Promise<Expedition> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/expeditions/')
        .subscribe((res: { 'message': Expedition }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  getAviary(): Promise<Aviary> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/pigeons/')
        .subscribe((res: { 'message': Aviary }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  postBuyPigeon(level: number, type: number): Promise<Expedition> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/pigeons/', `exp_lvl=${level}&exp_type=${type}`)
        .subscribe((res: { 'message': Expedition }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  postSellPigeon(pigeonId: number): Promise<{user :User, pigeon :Pigeon}> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/pigeons/sell', `p_id=${pigeonId}`)
        .subscribe((res: {user : User,pigeon: Pigeon }) => {
          resolve(res)
        }, err => {
          reject(err);
        });
    });
  }
  postSetDefenseTeam(): Promise<User> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/player/changedefenseteam', ``)
        .subscribe((res: {'message' : {user :User} }) => {
          resolve(res.message.user)
        }, err => {
          reject(err);
        });
    });
  }
  postOpenCard(pigeonId: number): Promise<Pigeon> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/pigeons/activate', `p_id=${pigeonId}`)
        .subscribe((res: { 'message': Pigeon }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  toggleTeam(pigeonId: number, team: 'A' | 'B'): Promise<any> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/pigeons/team' + team.toLocaleLowerCase(), `p_id=${pigeonId}`)
        .subscribe((res: { 'message': Pigeon }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }

}
