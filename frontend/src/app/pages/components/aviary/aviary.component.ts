import { Component, OnInit } from '@angular/core';
import { Level, Player } from 'src/app/core/models';
import { Pigeon } from 'src/app/core/models/pigeon';
import { ExpeditionsService } from 'src/app/core/services';
import { 
  faPlus, 
  faMinus, 
  faHatWizard,
  faFeatherAlt,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';
import { SortEnum } from 'src/app/core/models/sort-enum';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';

@Component({
  selector: 'app',
  templateUrl: './aviary.component.html',
  styleUrls: ['./aviary.component.scss']
})
export class AviaryComponent implements OnInit {
  faPlus = faPlus
  faMinus = faMinus
  faHatWizard = faHatWizard
  faShieldAlt = faShieldAlt
  faFistRaised = faFistRaised
  faFeatherAlt = faFeatherAlt;
  pigeons: Pigeon[];
  teamAPigeons: Pigeon[];
  teamBPigeons: Pigeon[];
  player: Player;
  nbInTeamA = 0;
  nbInTeamB = 0;
  sumTeamAAttack : number = 0;
  sumTeamBAttack : number = 0;
  sumTeamAMagic : number = 0;
  sumTeamBMagic : number = 0;
  sumTeamAShield : number = 0;
  sumTeamBShield : number = 0;
  selectOrderValues = [
    {
      key : 'default',
      value : SortEnum.default
    },
    {
      key : 'luckAndLevel',
      value : SortEnum.luckAndLevel
    },
    {
      key : 'attack',
      value : SortEnum.attack
    },
    {
      key : 'magic',
      value : SortEnum.magic
    },
    {
      key : 'shield',
      value : SortEnum.shield
    },
    {
      key : 'feathers',
      value : SortEnum.feathers
    },
    {
      key : 'team_a',
      value : SortEnum.team_a
    },
    {
      key : 'team_b',
      value : SortEnum.team_b
    },
    {
      key : 'droppings',
      value : SortEnum.droppings
    }
  ]
  sortBy: SortEnum
  levelList: Level[] = (lvlInfo as any).default;
  level : Level;

  constructor(private pigeonService: ExpeditionsService) {
  }

  ngOnInit(): void {
    this.pigeonService.getAviary().then((value) => {
      this.pigeons = value.pigeons.sort((a, b) => b.id - a.id);
      this.player = value.user.player;
      this.level = this.levelList[this.player.lvl - 1]
      this.teamAPigeons = this.pigeons.filter((pigeonInTab) => pigeonInTab.is_in_team_A)
      this.teamBPigeons = this.pigeons.filter((pigeonInTab) => pigeonInTab.is_in_team_B)
      this.nbInTeamA = this.teamAPigeons.length;
      this.nbInTeamB = this.teamBPigeons.length;
      this.sumTeamAAttack = this.sumValueOfPigeons(this.teamAPigeons, 'phys_atk')
      this.sumTeamBAttack = this.sumValueOfPigeons(this.teamBPigeons, 'phys_atk')
      this.sumTeamAMagic = this.sumValueOfPigeons(this.teamAPigeons, 'magic_atk')
      this.sumTeamBMagic = this.sumValueOfPigeons(this.teamBPigeons, 'magic_atk')
      this.sumTeamAShield = this.sumValueOfPigeons(this.teamAPigeons, 'shield')
      this.sumTeamBShield = this.sumValueOfPigeons(this.teamBPigeons, 'shield')
    })
  }
  setDefenseTeam(){
    this.pigeonService.postSetDefenseTeam().then((response)=>{
      this.player = response.player
    })
  }

  sumValueOfPigeons(pigeonList: Pigeon[], valueToSum: string){
    const defaultValue = 0
    return pigeonList
    .map(pigeons=>pigeons[valueToSum])
    .reduce(
      (accumulator, currentValue) => accumulator + currentValue,
      defaultValue
    );
  }

  sellPigeon(pigeon: Pigeon) {
    this.pigeonService.postSellPigeon(pigeon.id).then((response) => {
      this.player = response.user.player
      const index = this.pigeons.indexOf(pigeon);
      this.pigeons.splice(index, 1)
    })
  }

  openCard(pigeon: Pigeon) {
    this.pigeonService.postOpenCard(pigeon.id).then((value) => {
      const index = this.pigeons.indexOf(pigeon);
      this.pigeons[index] = value.pigeon
    })
  }

  selectFilter(value: string) {
    this.sortBy = SortEnum[value]
  }

  toggleTeam(pigeon: Pigeon, team: 'A' | 'B') {
    const index = this.pigeons.indexOf(pigeon);
    if (team === 'A') {
      this.pigeonService.toggleTeam(pigeon.id, 'A').then((value) => {
        this.pigeons[index] = value.pigeon;
        if (value.pigeon.is_in_team_A) {
          this.nbInTeamA++;
        } else {
          this.nbInTeamA--;
        }
       this.teamAPigeons = this.pigeons.filter((pigeonInTab) => pigeonInTab.is_in_team_A)
       this.sumTeamAAttack = this.sumValueOfPigeons(this.teamAPigeons, 'phys_atk')
       this.sumTeamAMagic = this.sumValueOfPigeons(this.teamAPigeons, 'magic_atk')
       this.sumTeamAShield = this.sumValueOfPigeons(this.teamAPigeons, 'shield')
      })
    }
    else {
      this.pigeonService.toggleTeam(pigeon.id, 'B').then((value) => {
        this.pigeons[index] = value.pigeon;
        if (value.pigeon.is_in_team_B) {
          this.nbInTeamB++;
        } else {
          this.nbInTeamB--;
        }
        this.teamBPigeons = this.pigeons.filter((pigeonInTab) => pigeonInTab.is_in_team_B)
        this.sumTeamBAttack = this.sumValueOfPigeons(this.teamBPigeons, 'phys_atk')
        this.sumTeamBMagic = this.sumValueOfPigeons(this.teamBPigeons, 'magic_atk')
        this.sumTeamBShield = this.sumValueOfPigeons(this.teamBPigeons, 'shield')
      })
    }
  }
}
