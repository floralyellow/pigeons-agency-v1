import { Component, OnDestroy, OnInit } from '@angular/core';
import { Level, Player } from 'src/app/core/models';
import { Expedition, Pigeon } from 'src/app/core/models';
import { ExpeditionsService } from 'src/app/core/services';
import * as expeditionInfo from 'src/assets/jsons/tr_expedition.json';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';

import {
  faHatWizard,
  faQuestion,
  faShieldAlt,
  faFistRaised,
  faEgg,
  faCrow,
  faExclamationTriangle,
  faSeedling
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-expeditions',
  templateUrl: './expeditions.component.html',
  styleUrls: ['./expeditions.component.scss']
})
export class ExpeditionsComponent implements OnInit, OnDestroy {
  faHatWizard = faHatWizard;
  faShieldAlt = faShieldAlt;
  faFistRaised = faFistRaised;
  faSeedling = faSeedling;
  faQuestion = faQuestion;
  faEgg = faEgg;
  faBird = faCrow;
  faExclamationTriangle = faExclamationTriangle;
  expeditionList: Expedition[] = (expeditionInfo as any).default;
  levelList: Level[] = (lvlInfo as any).default;
  expeditions: Pigeon[];
  info: Expedition;
  player: Player;
  level: Level;
  seeds: number;
  timeout;
  pigeonType = [faFistRaised, faHatWizard, faShieldAlt, faQuestion]
  top : number
  check = 1
  listBelowPlayerLevel
  listHigherThanPlayerLevel
  visible = false
  constructor(private expeditionService: ExpeditionsService) {
   
  }
  async ngOnInit() {
    this.info = await this.expeditionService.getExpeditionInfo();
    this.expeditions = this.info.expeditions;
    this.player = this.info.user.player;
    this.level = this.levelList[this.player.lvl - 1]
    this.seeds = this.player.seeds;
    this.getCurrentSeeds();
    this.listBelowPlayerLevel = this.expeditionList.filter((x,index)=>{
      return index < (this.player.lvl - 1)
    })
    this.listHigherThanPlayerLevel = this.expeditionList.filter((x,index)=>{
      return index >= (this.player.lvl - 1)
    })
  }

  ngOnDestroy(): void {
    clearTimeout(this.timeout)
  }

  buyPigeon(level: number, type: number) {
    this.expeditionService.postBuyPigeon(level, type).then((value: Expedition) => {
      if (typeof (value.expeditions) !== 'string') {
        this.expeditions.push(value.expeditions[value.expeditions.length - 1]);
        this.player = value.user.player;
        this.level = this.levelList[this.player.lvl - 1];
        this.seeds = this.player.seeds;
        this.getCurrentSeeds();
      }
    })
  }
  growDiv(id: string) {
    let growDiv = document.getElementById(id);
    if (growDiv.clientHeight) {
      growDiv.style.height = '0';
    } else {
      var wrapper = document.querySelector('.measuringWrapper');
      growDiv.style.height = (wrapper.clientHeight + 20) + "px";
    }
  }

  getCurrentSeeds() {
    (this.timeout !== undefined) ? clearTimeout(this.timeout) : null;
    if (this.seeds < this.level.max_seeds) {
      this.timeout = setTimeout(() => {
        this.seeds = Math.min(
          this.seeds + Math.round(this.level.seeds_minute / 60),
          this.level.max_seeds);
        this.getCurrentSeeds()
      }, 1000);
    }
  }
}
