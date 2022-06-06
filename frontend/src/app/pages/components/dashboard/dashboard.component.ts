import { Component, OnInit } from '@angular/core';
import {PlayerService} from 'src/app/core/services/player.service'
import {Level} from 'src/app/core/models/level'
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';
import { GlobalInfo } from 'src/app/core/models/global-info';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  player : GlobalInfo; 
  levelList: Level[] = (lvlInfo as any).default;
  level:Level;
  timeout;
  seeds : number;
  droppings : number;
  constructor(playerService : PlayerService ) {
    playerService.getPlayerInfo().then((value : GlobalInfo) => {
      this.player = value;
      this.level = this.levelList[this.player.user.player.lvl - 1]
      this.seeds = value.user.player.seeds;
      this.droppings = value.user.player.droppings;
      this.getCurrentSeedsAndDroppings()
    })
  }

  ngOnInit(): void {
  
  }

  getCurrentSeedsAndDroppings(){
    (this.timeout !== undefined)?clearTimeout(this.timeout):null;
    if(this.seeds < this.level.max_seeds || this.droppings < this.level.max_droppings){
      this.timeout = setTimeout(()=>{
        if (this.seeds < this.level.max_seeds) {
          this.seeds = Math.min(
            this.seeds + Math.ceil(this.level.seeds_minute / 60),
            this.level.max_seeds);
        }
        if (this.droppings < this.level.max_droppings) {
          this.droppings = Math.min(
            this.droppings + Math.ceil(this.player.droppings_minute / 60),
            this.level.max_droppings);
        }
        this.getCurrentSeedsAndDroppings()
      },1000);
    }
  }
}
