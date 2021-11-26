import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { GlobalInfo } from '../models/global-info';

@Injectable()
export class UpgradeService {

  constructor(private http: HttpClient) { }

  postSwapDroppingsWithSeeds(){
    return new Promise<GlobalInfo>((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/player/usebucket','')
          .subscribe((res: {'message' :GlobalInfo}) => {
            resolve(res.message)
          }, err => {
              reject(err); 
          });
    });
  }

  postLevelUp(){
    return new Promise<GlobalInfo>((resolve, reject) => {
      this.http.post(environment.apiBaseUrl + '/player/lvlup','')
          .subscribe((res: {'message' :GlobalInfo}) => {
            resolve(res.message)
          }, err => {
              reject(err); 
          });
    });
  }
}
