import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Expedition } from '../models';
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
              .subscribe((res: {'message' :Expedition}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  getAviary(): Promise<Aviary> {
      return new Promise((resolve, reject) => {
          this.http.get(environment.apiBaseUrl + '/pigeons/')
              .subscribe((res: {'message' :Aviary}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  postBuyPigeon(level:number, type: number): Promise<Expedition> {
      return new Promise((resolve, reject) => {
          this.http.post(environment.apiBaseUrl + '/pigeons/',`exp_lvl=${level}&exp_type=${type}`)
              .subscribe((res: {'message' :Expedition}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  postSellPigeon(pigeonId: number): Promise<Pigeon> {
      return new Promise((resolve, reject) => {
          this.http.post(environment.apiBaseUrl + '/pigeons/sell',`p_id=${pigeonId}`)
              .subscribe((res: {'message' :Pigeon}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  postOpenCard(pigeonId: number): Promise<Pigeon> {
      return new Promise((resolve, reject) => {
          this.http.post(environment.apiBaseUrl + '/pigeons/activate',`p_id=${pigeonId}`)
              .subscribe((res: {'message' :Pigeon}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  toggleTeam(pigeonId: number): Promise<any> {
      return new Promise((resolve, reject) => {
          this.http.post(environment.apiBaseUrl + '/pigeons/team',`p_id=${pigeonId}`)
              .subscribe((res: {'message' :Pigeon}) => {
                resolve(res.message)
              }, err => {
                  reject(err); 
              });
      });
  }
  
}
