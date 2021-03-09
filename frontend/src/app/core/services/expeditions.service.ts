import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Expedition } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ExpeditionsService {

  constructor(private http: HttpClient) { }
  getExpeditionInfo(): Promise<any> {
      return new Promise((resolve, reject) => {
          this.http.get(environment.apiBaseUrl + '/expeditions/')
              .subscribe((res: {'message' :Expedition}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  postBuyPigeon(level:number): Promise<any> {
      return new Promise((resolve, reject) => {
          this.http.post(environment.apiBaseUrl + '/pigeons/',`exp_lvl=${level}`)
              .subscribe((res: {'message' :Expedition}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
}
