import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Attack } from '../models/attack';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class MessagesService {

  constructor(private http: HttpClient) { }

  getHistory(): Promise<{ attacks: Attack[], user: User, users: User[] }> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/attackmessages')
        .subscribe((res: { 'message': { attacks: Attack[], user: User, users: User[]} }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }

  getHistoryDetail(id: number): Promise<{ attack: Attack }> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/attackmessagedetails',`a_id=${id}`)
        .subscribe((res: { 'message': { attack: Attack } }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
