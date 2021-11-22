import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {  Player } from 'src/app/core/models';
import { Aviary } from 'src/app/core/models/aviary';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';

@Component({
  selector: 'app-aviary',
  templateUrl: './aviary.component.html',
  styleUrls: ['./aviary.component.scss']
})
export class AviaryComponent implements OnInit {
  pigeons: Pigeon[];
  player: Player;
  nbInTeam = 0;
  constructor(private pigeonService: ExpeditionsService) {
    pigeonService.getAviary().then((value : Aviary) => {
      this.pigeons = value.pigeons;
      this.player = value.user.player;
      this.nbInTeam = this.pigeons.filter((pigeonInTab)=>pigeonInTab.is_in_team === true).length;
    })
   }

  ngOnInit(): void {
  }

  sellPigeon(pigeon : Pigeon){
    this.pigeonService.postSellPigeon(pigeon.id).then((value : Pigeon) => {
      const index = this.pigeons.indexOf(pigeon);
      this.pigeons.splice(index,1)
    })
  }

  openCard(pigeon : Pigeon){
    this.pigeonService.postOpenCard(pigeon.id).then((value : Pigeon) => {
      const index = this.pigeons.indexOf(pigeon);
      this.pigeons[index] = value
    })
  }

  toggleTeam(pigeon : Pigeon){
    const index = this.pigeons.indexOf(pigeon);
    if (
      this.nbInTeam >= 5 &&
      this.pigeons[index].is_in_team === false
    ){
      return false;
    }
    this.pigeonService.toggleTeam(pigeon.id).then((value : Pigeon) => {
      this.pigeons[index] = value;
      if(value.is_in_team){
        this.nbInTeam ++;
      } else {
        this.nbInTeam --;
      }
    })
  }
}
