import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
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
export class AdventureComponent implements OnInit , OnDestroy{
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
      console.log(this.currentAdventure)
      this.adventurePigeons = result.adventure_pigeons
      this.user = result.user
      this.level = this.levelList[(this.user.player.lvl - 1)]
      this.currentDroppingsMinute = result.droppings_minute
      this.currentDroppings = this.user.player.droppings
      this.getCurrentDroppings()
    })
  }

  ngOnDestroy(): void {
    clearTimeout(this.timeout)
  }

  attackWithTeam(team : 'A'|'B') {
    this.adventureService.postAttackCurrentAdventure(team).then(result => {
      this.currentAdventure = result.next_adventure
      this.adventurePigeons = result.next_adventure_pigeons
      this.modal.toggleModal()
      this.adventureAttack = result.adventure_attack
      this.modalTitle = (result.adventure_attack.is_victory === true)? 
        `Victory ! You won ${this.currentAdventure.reward_droppings} droppings !` : 
        'Defeat !'
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
      this.user = result.user
      this.currentDroppingsMinute = result.droppings_minute
      this.currentDroppings = this.user.player.droppings
      clearTimeout(this.timeout)
      this.getCurrentDroppings()
    })
  }

  getCurrentDroppings() {
    if (this.currentDroppings < this.level.max_droppings) {
      this.timeout = setTimeout(() => {
        this.currentDroppings = Math.min(
          (this.currentDroppings + Math.round(this.currentDroppingsMinute / 60)),
          this.level.max_droppings);
        this.getCurrentDroppings()
      }, 1000);
    }
  }
}
