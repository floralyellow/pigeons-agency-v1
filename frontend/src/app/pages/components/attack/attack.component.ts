import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { Pigeon, User } from 'src/app/core/models';
import { Attack } from 'src/app/core/models/attack';
import { AttackService } from 'src/app/core/services/attack.service';
import { ModalComponent } from 'src/app/ui';
import {
  faHatWizard,
  faShieldAlt,
  faFistRaised
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-attack',
  templateUrl: './attack.component.html',
  styleUrls: ['./attack.component.scss']
})
export class AttackComponent implements OnInit , OnDestroy{
  faHatWizard = faHatWizard;
  faFistRaised = faFistRaised;
  faShieldAlt = faShieldAlt;
  modalTitle: string;
  modalContent: string;
  attackResultDescription: string;
  modalHeaderBackground: string;
  users : User[]
  currentUser : User
  attackResult : Attack
  attackPigeons : Pigeon[]
  defendPigeons : Pigeon[]
  DELAY_SECONDS_BETWEEN_ATTACKS = 120
  interval = null
  attackerBlocked = 0
  defenderBlocked = 0

  @ViewChild(ModalComponent) modal;
  constructor( private attackService : AttackService){

  }
  ngOnInit() {
    this.attackService.getUsers().then(res => {
      this.users = res.users
      this.currentUser = res.user
      this.dateUpdate()
    })
  }

  ngOnDestroy(): void {
    clearInterval(this.interval)
  }

  attackButtonAction(team: 'A'|'B', targetId:number) {
    this.attackService.postAttack(team,targetId).then(res=>{
      this.attackerBlocked = Math.min(
        (res.attack.atk_shield_value * res.attack.atk_shield_blocs),
        res.attack.def_tot_phys
      )
      this.defenderBlocked = Math.min(
        (res.attack.def_shield_value * res.attack.def_shield_blocs),
        res.attack.atk_tot_phys 
      )
      this.users = res.users
      this.attackResult = res.attack
      this.currentUser = res.user
      this.attackPigeons = res.attack_pigeons
      this.defendPigeons = res.defend_pigeons
      this.modal.toggleModal();
      this.attackResultDescription = (res.attack.winner_id === this.currentUser.player.id)? 
        `You won ${Math.abs(res.attack.stolen_droppings)} droppings and ${res.attack.atk_new_military_score - res.attack.atk_old_military_score} military points !`
        : ` You lost ${Math.abs(res.attack.stolen_droppings)} droppings and ${res.attack.atk_old_military_score - res.attack.atk_new_military_score} military points !`
      this.modalTitle = (res.attack.winner_id === this.currentUser.player.id)? 
        `Victory !` : 
        `Defeat !`
      this.modalHeaderBackground = (res.attack.winner_id === this.currentUser.player.id)? 
        'has-background-success' : 'has-background-danger';
    })
  }

  isDefendTeamProtected(date: string) {
    return new Date(date).getTime() > new Date().getTime()
  }

  isNextAttackPossible(date: string) {
    return (new Date(date).getTime() + this.DELAY_SECONDS_BETWEEN_ATTACKS * 1000) > new Date().getTime()
  }

  dateUpdate(){
    this.interval = setInterval(()=>{},1000)
  }
}
