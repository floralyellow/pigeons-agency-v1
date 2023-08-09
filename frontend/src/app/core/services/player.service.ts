import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { GlobalInfo } from '../models/global-info';

@Injectable()
export class PlayerService {

  constructor(private http: HttpClient) { }

  getPlayerInfo(): Promise<GlobalInfo> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/player/')
        .subscribe((res: { 'message': GlobalInfo }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  setDarkMode(): Promise<GlobalInfo> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/player/changedarkmode', ``)
        .subscribe((res: { 'message': GlobalInfo }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
  isTutorialDone(): Promise<GlobalInfo> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/player/dotutorial', ``)
        .subscribe((res: { 'message': GlobalInfo }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
