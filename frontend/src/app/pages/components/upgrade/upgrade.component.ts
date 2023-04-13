import { Component, OnInit } from '@angular/core';
import { Level } from 'src/app/core/models';
import { GlobalInfo } from 'src/app/core/models/global-info';
import { PlayerService, UpgradeService } from 'src/app/core/services';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';
import { faPoop } from '@fortawesome/free-solid-svg-icons';
import { faFeatherAlt } from '@fortawesome/free-solid-svg-icons';

const NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO : number = 0.5;

@Component({
  selector: 'app-upgrade',
  templateUrl: './upgrade.component.html',
  styleUrls: ['./upgrade.component.scss']
})
export class UpgradeComponent implements OnInit {
  faPoop = faPoop;
  faFeatherAlt = faFeatherAlt;
  playerInfo : GlobalInfo;
  levelList: Level[] = (lvlInfo as any).default;
  level:Level;
  timeout;
  seeds : number;
  droppings : number;
  droppings_needed_to_buy_bucket : number;

  constructor(private playerService : PlayerService, private upgradeService : UpgradeService) {
    this.playerService.getPlayerInfo().then(data => {
      this.playerInfo = data;
      this.level = this.levelList[this.playerInfo.user.player.lvl - 1]
      this.seeds = data.user.player.seeds;
      this.droppings = data.user.player.droppings;
      this.droppings_needed_to_buy_bucket = Math.trunc(this.level.max_droppings * NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO)
      this.getCurrentSeedsAndDroppings();
    })
  }

  ngOnInit(): void {
  }

  exchangeDroppingsWithSeeds(){
    this.upgradeService.postSwapDroppingsWithSeeds().then(data => {
      this.playerInfo = data;
      this.seeds = data.user.player.seeds;
      this.droppings = data.user.player.droppings;
      this.getCurrentSeedsAndDroppings();
    })
  }

  levelUp(){
    this.upgradeService.postLevelUp().then(data => {
      this.playerInfo = data;
      this.level = this.levelList[this.playerInfo.user.player.lvl - 1]
      this.seeds = data.user.player.seeds;
      this.droppings = data.user.player.droppings;
      this.droppings_needed_to_buy_bucket = Math.trunc(this.level.max_droppings * NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO)
      this.getCurrentSeedsAndDroppings();
    })
  }
  
  getCurrentSeedsAndDroppings(){
    (this.timeout !== undefined)?clearTimeout(this.timeout):null;
    if(this.seeds < this.level.max_seeds || this.droppings < this.level.max_droppings){
      this.timeout = setTimeout(()=>{
        if (this.seeds < this.level.max_seeds) {
          this.seeds = Math.min(
            this.seeds + (this.level.seeds_minute / 60),
            this.level.max_seeds);
        }
        if (this.droppings < this.level.max_droppings) {
          this.droppings = Math.min(
            this.droppings + (this.playerInfo.droppings_minute / 60),
            this.level.max_droppings);
        }
        this.getCurrentSeedsAndDroppings()
      },1000);
    }
  }
}
