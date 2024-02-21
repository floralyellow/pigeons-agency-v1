import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Pigeon, Adventure, User, AdventureAttack } from '../models';
import { GlobalInfo } from '../models/global-info';
@Injectable({
  providedIn: 'root'
})
export class AdventureService {

  constructor(private http: HttpClient) { }

  getCurrentAdventure(): Promise<{ user :User, droppings_minute: number, adventure: Adventure, adventure_pigeons: Pigeon[] }> {
    return new Promise((resolve, reject) => {
      this.http.get(environment.apiBaseUrl + '/adventure')
        .subscribe((res: { 'message': { user :User, droppings_minute: number, adventure: Adventure, adventure_pigeons: Pigeon[] } }) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }

  postAttackCurrentAdventure(team : 'A'|'B'): Promise<{ 
    user :User, 
    droppings_minute :number
    adventure_attack: AdventureAttack,
    current_adventure: Adventure,
    next_adventure: Adventure,
    next_adventure_pigeons: Pigeon[]
  }> {
    return new Promise((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/adventure', `a_team=${team}`)
        .subscribe((res: { 'message': { 
          user :User, 
          droppings_minute :number, 
          adventure_attack: AdventureAttack,
          current_adventure: Adventure,
          next_adventure: Adventure,
          next_adventure_pigeons: Pigeon[]
        }}) => {
          resolve(res.message)
        }, err => {
          reject(err);
        });
    });
  }
}
