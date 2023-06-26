import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/core/models';
import { AttackService } from 'src/app/core/services/attack.service';

@Component({
  selector: 'app-attack',
  templateUrl: './attack.component.html',
  styleUrls: ['./attack.component.scss']
})
export class AttackComponent implements OnInit {
  users : User[]
  currentUser : User
  constructor( private attackService : AttackService){

  }
  async ngOnInit() {
    this.users = (await this.attackService.getUsers()).users
    this.currentUser = (await this.attackService.getUsers()).user
  }
}
