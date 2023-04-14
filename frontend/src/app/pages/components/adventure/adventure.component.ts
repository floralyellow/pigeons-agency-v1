import { Component, OnInit, ViewChild } from '@angular/core';
import { Adventure, AdventureAttack, Level, Pigeon, User } from 'src/app/core/models';
import { AdventureService } from 'src/app/core/services';
import { ModalComponent } from 'src/app/ui';
import {
  faHatWizard,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';
import * as lvlInfo from 'src/assets/jsons/tr_lvl_info.json';
import { GlobalInfo } from 'src/app/core/models/global-info';

@Component({
  selector: 'app-adventure',
  templateUrl: './adventure.component.html',
  styleUrls: ['./adventure.component.scss']
})
export class AdventureComponent implements OnInit {
  faHatWizard = faHatWizard;
  faFistRaised = faFistRaised;
  faShieldAlt = faShieldAlt;
  currentAdventure: Adventure;
  adventurePigeons : Pigeon[];
  @ViewChild(ModalComponent) modal! : ModalComponent
  modalTitle: string;
  modalContent: string;
  modalHeaderBackground: string;
  adventureAttack: AdventureAttack;
  pveBlocked : number;
  attackerBlocked : number;
  user: User;
  levelList: Level[] = (lvlInfo as any).default;
  timeout;
  currentDroppingsMinute = 0
  currentDroppings = 0
  level : Level
  playerInfo : GlobalInfo;
  
  constructor(private adventureService : AdventureService) { }

  ngOnInit(): void {
    this.adventureService.getCurrentAdventure().then(result => {
      this.currentAdventure = result.adventure
      this.adventurePigeons = result.adventure_pigeons
      this.user = result.user
      this.level = this.levelList[(this.user.player.lvl - 1)]
      this.currentDroppingsMinute = result.droppings_minute
      this.getCurrentDroppings()
    })
  }

  attackWithTeam(team : 'A'|'B') {
    this.adventureService.postAttackCurrentAdventure(team).then(result => {
      this.currentAdventure = result.next_adventure
      this.adventurePigeons = result.next_adventure_pigeons
      this.modal.toggleModal()
      this.adventureAttack = result.adventure_attack
      this.modalTitle = (result.adventure_attack.is_victory === true)? 'Victory !' : 'Defeat !'
      this.modalHeaderBackground = (result.adventure_attack.is_victory === true)? 
        'has-background-success' : 'has-background-danger';
      this.attackerBlocked = Math.min(
        (this.adventureAttack.atk_shield_value * this.adventureAttack.atk_shield_blocs),
        this.adventureAttack.def_tot_phys
      )
      this.pveBlocked = Math.min(
        (this.adventureAttack.def_shield_value * this.adventureAttack.def_shield_blocs),
        this.adventureAttack.atk_tot_phys 
      )
      this.user = result.globalInfo.user
      this.currentDroppingsMinute = result.globalInfo.droppings_minute
      this.getCurrentDroppings()
    })
  }

  getCurrentDroppings() {
    (this.timeout !== undefined) ? clearTimeout(this.timeout) : null;
    if (this.user.player.droppings < this.level.max_droppings) {
      this.timeout = setTimeout(() => {
        this.currentDroppings = Math.min(
          this.user.player.droppings + Math.round(this.currentDroppingsMinute / 60), //missing dropping minute in data
          this.level.max_droppings);
        this.getCurrentDroppings()
      }, 1000);
    }
  }
}
