import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {

  constructor(private http: HttpClient) { }

  login(): Promise<any> {
      return new Promise((resolve, reject) => {
          this.http.get(environment.apiBaseUrl + '/token/', {})
              .subscribe((res: {}) => {
                  resolve(res);
              }, err => {
                  reject(err); 
              });
      });
  }
}
