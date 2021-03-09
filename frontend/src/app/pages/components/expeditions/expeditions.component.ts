import { Component, OnInit } from '@angular/core';
import { Level, Player } from 'src/app/core/models';
import { Expedition } from 'src/app/core/models/expedition';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';
import * as expeditionInfo from 'src/assets/jsons/tr_expedition.json';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';

@Component({
  selector: 'app-expeditions',
  templateUrl: './expeditions.component.html',
  styleUrls: ['./expeditions.component.scss']
})
export class ExpeditionsComponent implements OnInit {
  expeditionList:Expedition[] = (expeditionInfo as any).default;
  levelList: Level[] = (lvlInfo as any).default;
  expeditions: Pigeon[];
  info: Expedition;
  player: Player;
  level:Level;
  constructor(private expeditionService : ExpeditionsService) {
    expeditionService.getExpeditionInfo().then((value : Expedition) => {
      this.expeditions = value.expeditions;
      this.info = value;
      this.player = value.user.player;
      this.level = this.levelList[this.player.lvl - 1]
    })
  }

  ngOnInit(): void { 
  }

  buyPigeon(level : number){
    this.expeditionService.postBuyPigeon(level).then((value : Expedition) => {
      this.expeditions = value.expeditions;
      this.player = value.user.player;
      this.level = this.levelList[this.player.lvl - 1]
    })
  }

}
