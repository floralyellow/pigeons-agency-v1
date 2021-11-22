import { Component, OnDestroy, OnInit } from '@angular/core';
import { Level, Player } from 'src/app/core/models';
import { Expedition } from 'src/app/core/models/expedition';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';
import * as expeditionInfo from 'src/assets/jsons/tr_expedition.json';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';
import { faMagic } from '@fortawesome/free-solid-svg-icons';
import { faQuestion } from '@fortawesome/free-solid-svg-icons';
import { faShieldAlt } from '@fortawesome/free-solid-svg-icons';
import { faFistRaised } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-expeditions',
  templateUrl: './expeditions.component.html',
  styleUrls: ['./expeditions.component.scss']
})
export class ExpeditionsComponent implements OnInit, OnDestroy {
  faMagic = faMagic;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faQuestion = faQuestion;
  expeditionList:Expedition[] = (expeditionInfo as any).default;
  levelList: Level[] = (lvlInfo as any).default;
  expeditions: Pigeon[];
  info: Expedition;
  player: Player;
  level:Level;
  seeds:number;
  timeout;
  pigeonType = [faFistRaised,faMagic,faShieldAlt,faQuestion]
  constructor(private expeditionService : ExpeditionsService) {
    expeditionService.getExpeditionInfo().then((value : Expedition) => {
      this.expeditions = value.expeditions;
      this.info = value;
      this.player = value.user.player;
      this.level = this.levelList[this.player.lvl - 1]
      this.seeds = this.player.seeds;
      this.getCurrentSeeds();
    })
  }

  ngOnInit(): void { 
  }
  ngOnDestroy(): void { 
  }

  buyPigeon(level : number, type: number){
    this.expeditionService.postBuyPigeon(level, type).then((value : Expedition) => {
      this.expeditions = value.expeditions;
      this.player = value.user.player;
      this.level = this.levelList[this.player.lvl - 1];
      this.seeds = this.player.seeds;
    })
    this.getCurrentSeeds();
  }
  getCurrentSeeds(){
    (this.timeout !== undefined)?clearTimeout(this.timeout):null;
    if(this.seeds < this.level.max_seeds){
      this.timeout = setTimeout(()=>{
        this.seeds = Math.min(
          this.seeds + Math.round(this.level.seeds_minute / 60),
          this.level.max_seeds);
        this.getCurrentSeeds()
      },1000);
    }
  }
}
