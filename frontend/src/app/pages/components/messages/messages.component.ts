import { Component, OnInit, ViewChild } from '@angular/core';

import {
  faEye,
  faHatWizard,
  faFistRaised,
  faShieldAlt
} from '@fortawesome/free-solid-svg-icons';
import { Pigeon, Attack } from 'src/app/core/models';
import { User } from 'src/app/core/models/user';
import { MessagesService } from 'src/app/core/services';
import { ModalComponent } from 'src/app/ui';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.scss']
})
export class MessagesComponent implements OnInit {
  messages: Attack[];
  user: User;
  userList: User[];
  attackPigeons: Pigeon[];
  defensePigeons: Pigeon[];
  attackResult:Attack;
  faEye = faEye;
  faHatWizard = faHatWizard;
  faFistRaised = faFistRaised;
  faShieldAlt = faShieldAlt;
  attackResultDescription: string;
  attackerBlocked = 0
  defenderBlocked = 0
  
  @ViewChild(ModalComponent) modal;
  modalTitle: string;
  modalContent: string;
  modalHeaderBackground: string;

  constructor(private messagesService : MessagesService){}

   ngOnInit(){
    this.messagesService.getHistory().then(data=>{
      this.messages = data.attacks;
      this.user = data.user;
      this.userList = data.users;
    })
  }

  getUser(id: number){
    return id === this.user.player.id ? 'You' : this.userList.filter(user=>user.player.id === id)[0].username
  }

  async openModal(id: number){
    this.messagesService.getHistoryDetail(id).then( res => {
      this.attackerBlocked = Math.min(
        (res.attack.atk_shield_value * res.attack.atk_shield_blocs),
        res.attack.def_tot_phys
      )
      this.defenderBlocked = Math.min(
        (res.attack.def_shield_value * res.attack.def_shield_blocs),
        res.attack.atk_tot_phys 
      )
      this.attackResult = res.attack;
      this.attackPigeons = res.attack_pigeons;
      this.defensePigeons = res.defend_pigeons;
      this.modalTitle = (res.attack.winner_id === this.user.player.id)? 
      `Victory !` : 
      `Defeat !`
      const militaryMovements = (this.user.player.id === res.attack.attacker) ? res.attack.atk_new_military_score - res.attack.atk_old_military_score: res.attack.def_new_military_score - res.attack.def_old_military_score
      this.attackResultDescription = (res.attack.winner_id === this.user.player.id)? 
        `You won ${Math.abs(res.attack.stolen_droppings)} droppings and ${militaryMovements} military points !`
        : ` You lost ${Math.abs(res.attack.stolen_droppings)} droppings and ${militaryMovements} military points !`
    this.modalHeaderBackground = (res.attack.winner_id === this.user.player.id)? 
      'has-background-success' : 'has-background-danger';
      this.modal.toggleModal();
    })
  }
}
