import { Component, OnInit } from '@angular/core';
import { Player } from 'src/app/core/models/player';
import {PlayerService} from 'src/app/core/services/player.service'
import {Level} from 'src/app/core/models/level'
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  player : Player; 
  levelList: Level[] = (lvlInfo as any).default;
  level:Level;
  constructor(playerService : PlayerService ) {
    playerService.getPlayerInfo().then((value : Player) => {
      this.player = value;
      this.level = this.levelList[this.player.user.player.lvl - 1]
    })
  }

  ngOnInit(): void {
  
  }

}
