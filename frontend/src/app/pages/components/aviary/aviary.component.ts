import { Component, OnInit } from '@angular/core';
import {  Player } from 'src/app/core/models';
import { Aviary } from 'src/app/core/models/aviary';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-aviary',
  templateUrl: './aviary.component.html',
  styleUrls: ['./aviary.component.scss']
})
export class AviaryComponent implements OnInit {
  faPlus = faPlus
  faMinus = faMinus
  pigeons: Pigeon[];
  player: Player;
  nbInTeamA = 0;
  nbInTeamB = 0;
  constructor(private pigeonService: ExpeditionsService) {
    pigeonService.getAviary().then((value : Aviary) => {
      this.pigeons = value.pigeons.sort((a,b)=>b.id - a.id);
      this.player = value.user.player;
      this.nbInTeamA = this.pigeons.filter((pigeonInTab)=>pigeonInTab.is_in_team_A === true).length;
      this.nbInTeamB = this.pigeons.filter((pigeonInTab)=>pigeonInTab.is_in_team_B === true).length;
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

  toggleTeam(pigeon : Pigeon, team: 'A'|'B'){
    const index = this.pigeons.indexOf(pigeon);
    if(team === 'A') {
      this.pigeonService.toggleTeam(pigeon.id,'A').then((value : Pigeon) => {
        this.pigeons[index] = value;
        if(value.is_in_team_A){
          this.nbInTeamA ++;
        } else {
          this.nbInTeamA --;
        }
      })
    }
    else{
      this.pigeonService.toggleTeam(pigeon.id,'B').then((value : Pigeon) => {
        this.pigeons[index] = value;
        if(value.is_in_team_B){
          this.nbInTeamB ++;
        } else {
          this.nbInTeamB --;
        }
      })
    }
  }
}
