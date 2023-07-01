import { Component, OnInit, ViewChild } from '@angular/core';
import { User } from 'src/app/core/models';
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
export class AttackComponent implements OnInit {
  faHatWizard = faHatWizard;
  faFistRaised = faFistRaised;
  faShieldAlt = faShieldAlt;
  modalTitle: string;
  modalContent: string;
  users : User[]
  currentUser : User
  attackResult : Attack
  @ViewChild(ModalComponent) modal;
  constructor( private attackService : AttackService){

  }
  ngOnInit() {
    this.attackService.getUsers().then(res => {
      this.users = res.users
      this.currentUser = res.user
    })
  }

  attackButtonAction(team: 'A'|'B', targetId:number) {
    this.attackService.postAttack(team,targetId).then(res=>{
      this.users = res.users
      this.attackResult = res.attack
      console.log(this.attackResult)
      this.modal.toggleModal();
      this.modalTitle = (res.attack.winner_id === this.currentUser.id)? 
        `Victory ! You won ${res.attack.stolen_droppings} droppings !` : 
        'Defeat ! You lost ${this.currentAdventure.reward_droppings} droppings !'
      this.modalHeaderBackground = (result.adventure_attack.is_victory === true)? 
        'has-background-success' : 'has-background-danger';
    })
  }
}
