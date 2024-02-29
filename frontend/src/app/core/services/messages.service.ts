import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Attack } from '../models/attack';
import { User } from '../models/user';
import { Pigeon } from '../models';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MessagesService {
  public nbMessage = new Subject<number>();
  value$ = this.nbMessage.asObservable();

  constructor(private http: HttpClient) { }

  updateMessageNumber(newValue: number): void {
    this.nbMessage.next(newValue);
  }

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

  getHistoryDetail(id: number): Promise<{ attack: Attack, attack_pigeons: Pigeon[], defend_pigeons: Pigeon[] }> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/attackmessagedetails',`a_id=${id}`)
        .subscribe((res: { 'message': { attack: Attack, attack_pigeons: Pigeon[], defend_pigeons: Pigeon[] } }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
