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
    return id === this.user.id ? 'You' : this.userList.filter(user=>user.id === id)[0].username
  }

  async openModal(id: number){
    this.messagesService.getHistoryDetail(id).then( res => {
      this.attackResult = res.attack;
      this.attackPigeons = res.attack_pigeons;
      this.defensePigeons = res.defend_pigeons;
      this.modalTitle = (res.attack.winner_id === this.user.id)? 
      `Victory ! You won ${res.attack.stolen_droppings} droppings !` : 
      `Defeat ! You lost ${res.attack.stolen_droppings} droppings !`
    this.modalHeaderBackground = (res.attack.winner_id === this.user.id)? 
      'has-background-success' : 'has-background-danger';
      this.modal.toggleModal();
    })
  }
}
