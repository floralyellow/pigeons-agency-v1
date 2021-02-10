import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Player } from '../models/player';

@Injectable()
export class PlayerService {

  constructor(private http: HttpClient) { }

  getPlayerInfo(): Promise<any> {
      return new Promise((resolve, reject) => {
          this.http.get(environment.apiBaseUrl + '/player/')
              .subscribe((res: {'message' :Player}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
}
